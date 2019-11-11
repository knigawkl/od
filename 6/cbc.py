import multiprocessing as mp
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


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
    iv = IV
    des = DES.new(key, IV=IV)
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


def de_mapper(i):
    offset = i * block_size
    block = bytes(shared_data[offset:offset + block_size])
    for j in range(1000):
        decrypted = des.decrypt(block)
        block = decrypted

    if i == 0:
        intermediate = xor64d(block, IV)
    else:
        intermediate = xor64d(block, shared_data[offset-block_size:offset])

    output_data[offset:offset + block_size] = intermediate


if __name__ == "__main__":
    plain_text = "alamakot" * 10000
    key = "haslo123"
    IV = get_random_bytes(8)
    block_size = 8
    no_blocks = len(plain_text) // block_size

    start = time.time()
    encryptedCBC = encrypt_CBC_serial(key, plain_text)
    print('CBC Encrypt time serial: ', (time.time() - start))

    des = DES.new(key, IV=IV)
    shared_data = mp.RawArray(ctypes.c_ubyte, encryptedCBC)
    output_data = mp.RawArray(ctypes.c_ubyte, encryptedCBC)
    pool = mp.Pool(8)

    start = time.time()
    pool.map(de_mapper, range(no_blocks))
    print('CBC Decrypt time para: ', time.time() - start)
    print(bytes(output_data))
