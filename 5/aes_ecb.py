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


plain_text = "alamakot" * 1000
key = "haslo123haslo123"
block_size = 16
no_blocks = int(len(plain_text) / block_size)
plain_text = bytearray(plain_text, 'utf-8')


def en_mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        encrypted = aes.encrypt(block)
        block = encrypted
    output_data[offset:offset + block_size] = bytearray(encrypted)
    return i


aes = AES.new(key, AES.MODE_ECB)
shared_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
output_data = multiprocessing.RawArray(ctypes.c_ubyte, plain_text)
pool = multiprocessing.Pool(8)
starttime = time.time()
pool.map(en_mapper, range(no_blocks))
print('ECB encrypt time parallel: ', (time.time() - starttime))
encrypted = bytes(output_data)


def de_mapper(i):
    offset = i * block_size
    block = bytes(share_data[offset:offset + block_size])
    for j in range(1000):
        decrypted = aes.decrypt(block)
        block = decrypted
    out_data[offset:offset + block_size] = bytearray(decrypted)
    return i


aes = AES.new(key, AES.MODE_ECB)
share_data = multiprocessing.RawArray(ctypes.c_char, encrypted)
out_data = multiprocessing.RawArray(ctypes.c_char, encrypted)
pool = multiprocessing.Pool(8)
starttime = time.time()
pool.map(de_mapper, range(no_blocks))
print('ECB Decrypt time para: ', (time.time() - starttime))
decrypted = bytes(out_data)
print(decrypted.decode('latin-1'))


def decrypt_ECB_serial(key, encrypted_block):
    vector = bytearray(encrypted_block)
    aes = AES.new(key, AES.MODE_ECB)
    for i in range(no_blocks):
        offset = i*block_size
        block = encrypted_block[offset:offset+block_size]
        for j in range(1000):
            decrypted = aes.decrypt(block)
            block = decrypted
        vector[offset:offset+block_size] = bytearray(decrypted)
    return bytes(vector)


starttime = time.time()
decrypted = decrypt_ECB_serial(key, encrypted)
print('ECB Decrypt time serial: ', (time.time() - starttime))
print(decrypted.decode('latin-1'))
