import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

iv_global = b'00011201'

def xor64(a, b):
    block = bytearray(a, 'utf-8')
    for j in range(8):
        block[j] = ord(a[j]) ^ b[j]
    return block

def xor64d(a, b):
    block = bytearray(a)
    for j in range(8):
        block[j] = a[j] ^ b[j]
    return block


def encrypt_CBC_serial(key, plain_text):
    vector = bytearray(plain_text, 'utf-8')
    iv = iv_global
    des = DES.new(key, IV=iv)
    for i in range(no_blocks):
        offset = i * block_size
        block = plain_text[offset:offset + block_size]
        intermediate = bytes(xor64(block, iv))
        for j in range(1000):
            encrypted = des.encrypt(intermediate)
            intermediate = encrypted
        vector[offset:offset + block_size] = bytearray(encrypted)
        iv = encrypted
    return bytes(vector)


plain_text = "alamakot" * 1000
key = "haslo123"

block_size = 8
no_blocks = len(plain_text) // block_size

starttime = time.time()
encryptedCBC = encrypt_CBC_serial(key, plain_text)
print(encryptedCBC)
print('CBC Encrypt time serial: ', (time.time() - starttime))
# print("Encrypted CBC: ", encryptedCBC)

des = DES.new(key, IV=iv_global)
def mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        decrypted = des.decrypt(block)
        block = decrypted

    if i == 0:
        intermediate = xor64d(block, iv_global)
    else:
        offset_prev = (i - 1) * block_size
        intermediate = xor64d(block, shit[offset_prev:offset_prev + block_size])

    output_data[offset:offset + block_size] = intermediate


shit = multiprocessing.RawArray(ctypes.c_ubyte, encryptedCBC)
shared_data = multiprocessing.RawArray(ctypes.c_ubyte, encryptedCBC)
output_data = multiprocessing.RawArray(ctypes.c_ubyte, encryptedCBC)

pool = multiprocessing.Pool(8)
print(no_blocks)

start = time.time()
pool.map(mapper, range(no_blocks))
end = time.time()

print(end - start)
print(bytes(output_data))
