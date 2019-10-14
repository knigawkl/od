"""
Porównaj wynik szyfrowania w trybach ECB i CBC. Jaka jest entropia kryptogramów?
"""
import math
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes


def calc_entropy(string):
    """Calculates the Shannon entropy of a string"""
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy


with open('../2/texts/written/letters/wwf12.txt', 'r') as file:
    plaintext = file.read().replace('\n', '')
print("plaintext: {}".format(calc_entropy(plaintext)))

iv = get_random_bytes(8)
des = DES.new("key12345", DES.MODE_CBC, iv)
encrypted_des_cbc = des.encrypt(plaintext)
iv = get_random_bytes(8)
des = DES.new("key12345", DES.MODE_ECB, iv)
encrypted_des_ecb = des.encrypt(plaintext)
print("DES CBC: {}".format(calc_entropy(encrypted_des_cbc)))
print("DES ECB: {}".format(calc_entropy(encrypted_des_ecb)))


iv = get_random_bytes(16)
aes = AES.new("key0123456781011", AES.MODE_CBC, iv)
encrypted_aes_cbc = aes.encrypt(plaintext)
iv = get_random_bytes(16)
aes = AES.new("key0123456781011", AES.MODE_ECB, iv)
encrypted_aes_ecb = aes.encrypt(plaintext)
print("AES CBC: {}".format(calc_entropy(encrypted_aes_cbc)))
print("AES ECB: {}".format(calc_entropy(encrypted_aes_ecb)))
