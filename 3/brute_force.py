from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from BMPencrypt import expand_data
from PIL import Image
import entropy
import itertools
import sys
import string

aes_password = "aaaaaafa"
filename = sys.argv[1]
iv = "a" * 16

img_in = Image.open(filename)
data = img_in.convert("RGB").tobytes()

'''file_original = open(filename, 'rb').read()
toAdd = 16 - len(file_original) % 16
if toAdd != 0:
    for i in range(toAdd):
        file_original += b'i'
file_encrypted = aes_crypter.encrypt(file_original)
print(entropy.getEntropy(file_original), entropy.getEntropy(file_encrypted))
'''
def decrypt(file, key):
    k = PBKDF2(key, b"abc")
    des_decrypt = AES.new(k, AES.MODE_CBC, iv)
    return des_decrypt.decrypt(file)

def attempt_brute_force(file):
    alf = string.ascii_lowercase
    possible_keys = itertools.product(alf, alf, alf)
    i = 0
    for key in possible_keys:
        e = entropy.getEntropy(decrypt(file[:160], ''.join(key)))
        print(''.join(key), e)
        if e < 6:
            i = Image.frombytes( "RGB",(800, 320), decrypt(data, ''.join(key)))
            i.show()
            return key

if __name__ == "__main__":

    print(attempt_brute_force(data))