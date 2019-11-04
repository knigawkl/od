import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def xor64(a, b):
    print(type(a))
    block = bytearray(a, 'latin-1')
    for j in range(8):
        block[j] = ord(a[j]) ^ b[j]
    return block


def encrypt_CBC_serial(key, plain_text, iv):
    vector = bytearray(plain_text, 'latin-1')
    for i in range(no_blocks):
        offset = i * block_size
        block = plain_text[offset:offset + block_size]
        intermediate = bytes(xor64(block, iv))
        for j in range(1000):
            encrypted = des.encrypt(intermediate)
            intermediate = encrypted
        encrypted = des.encrypt(intermediate)
        vector[offset:offset + block_size] = bytearray(encrypted)
        iv = encrypted
    return bytes(vector)



plain_text = "alamakot" * 1000
key = "haslo123"
iv = get_random_bytes(8)
des = DES.new(key, DES.MODE_CBC, iv)
ivr = iv
block_size = 8
no_blocks = int(len(plain_text) / block_size)

starttime = time.time()
encryptedCBC = encrypt_CBC_serial(key, plain_text, iv)
print('CBC Encrypt time serial: ', (time.time() - starttime))


# print("Encrypted CBC: ", encryptedCBC)


def de_mapper(i):
    offset = i * block_size
    block = bytes(share_data[offset:offset + block_size])
    '''
    for j in range(1000):
        decrypted = des.decrypt(block)
        block = decrypted
    '''
    decrypted = des.decrypt(block)
    #decrypted = xor64(share_data[offset - 8:offset + block_size - 8], decrypted)
    out_data[offset:offset + block_size] = bytearray(decrypted)
    return i


des = DES.new(key, DES.MODE_CBC, ivr)
share_data = multiprocessing.RawArray(ctypes.c_ubyte, encryptedCBC)
out_data = multiprocessing.RawArray(ctypes.c_ubyte, encryptedCBC)
pool = multiprocessing.Pool(8)
starttime = time.time()
pool.map(de_mapper, range(no_blocks))
print('cbc Decrypt time para: ', (time.time() - starttime))
decrypted = bytes(out_data)
print(decrypted.decode('latin-1'))
