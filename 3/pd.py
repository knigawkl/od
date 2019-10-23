import itertools
import math
import string

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from PIL import Image


def calc_entropy(string):
    """Calculates the Shannon entropy of a string"""
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy


def decrypt(file, key):
    iv = 'a'*16
    k = PBKDF2(key, b"abc")
    des_decrypt = AES.new(k, AES.MODE_CBC, iv)
    return des_decrypt.decrypt(file)


def bf(data):
    az = string.ascii_lowercase
    possible_keys = itertools.product(az, az, az)
    for key in possible_keys:
        e = calc_entropy(decrypt(data[:160], ''.join(key)))
        if e < 6:
            i = Image.frombytes("RGB", (800, 320), decrypt(data, ''.join(key)))
            i.show()
            return key


if __name__ == "__main__":
    print("Please wait...")
    file_name = 'we800_CBC_encrypted.bmp'
    img_in = Image.open(file_name)
    data = img_in.convert("RGB").tobytes()
    print(bf(data))
