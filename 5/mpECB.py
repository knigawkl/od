import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def encrypt_CBC_serial(key, plain_text, iv):
    vector = bytearray(plain_text, 'utf-8')
    des = DES.new(key, DES.MODE_CBC, iv)
    for i in range(no_blocks):
        offset = i * block_size
        block = plain_text[offset:offset + block_size]
        for j in range(1000):
            encrypted = des.encrypt(block)
            block = encrypted
        vector[offset:offset + block_size] = bytearray(encrypted)
    return bytes(vector)


def decrypt_CBC_serial(key, encrypted_block, iv):
    vector = bytearray(encrypted_block)
    des = DES.new(key, DES.MODE_CBC, iv)
    for i in range(no_blocks):
        offset = i * block_size
        block = encrypted_block[offset:offset + block_size]
        for j in range(1000):
            decrypted = des.decrypt(block)
            block = decrypted
        vector[offset:offset + block_size] = bytearray(decrypted)
    return bytes(vector)


plain_text = "alamakot" * 1000
key = "haslo123"
iv = get_random_bytes(8)
block_size = 8
no_blocks = int(len(plain_text) / block_size)

starttime = time.time()
encryptedECB = encrypt_CBC_serial(key, plain_text, iv)
print('ECB Encrypt time serial: ', (time.time() - starttime))

starttime = time.time()
decrypted = decrypt_CBC_serial(key, encryptedECB, iv)
print('ECB Decrypt time serial: ', (time.time() - starttime))
print(decrypted)
