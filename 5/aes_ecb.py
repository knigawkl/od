import multiprocessing
import time
import ctypes

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def xor64(a, b):
    block = bytearray(a, 'utf-8')
    for j in range(16):
        block[j] = ord(a[j]) ^ b[j]
    return block


def en_mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        encrypted = aes.encrypt(block)
        block = encrypted
    output_data[offset:offset + block_size] = bytearray(encrypted)
    return i


def de_mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        decrypted = aes.decrypt(block)
        block = decrypted
    output_data[offset:offset + block_size] = bytearray(decrypted)
    return i


plain_text = "alamakot" * 1000
key = "haslo123haslo123"
iv = get_random_bytes(16)
block_size = 16
no_blocks = int(len(plain_text) / block_size)
plain_text = bytearray(plain_text, 'utf-8')


aes = AES.new(key)
shared_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
output_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
pool = multiprocessing.Pool(8)
starttime = time.time()
pool.map(en_mapper, range(no_blocks))
print('ECB encrypt time parallel: ', (time.time() - starttime))
encrypted = bytes(output_data)


shared_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
output_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
pool = multiprocessing.Pool(8)
starttime = time.time()
pool.map(de_mapper, range(no_blocks))
print('ECB Decrypt time para: ', (time.time() - starttime))
decrypted = bytes(output_data)
print(decrypted.decode('latin-1'))
