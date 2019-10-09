"""
Zaimplementuj samodzielnie algorytm generowania klucza algorytmem RC4 i napisz program szyfrujący przy pomocy XOR i klucza generowanego przez RC4.
"""
from Crypto.Cipher import ARC4

ascii_length = 256


def create_key(keyword):
    keystream = []
    for c in keyword:
        keystream.append(ord(c))
    s = [i for i in range(ascii_length)]
    j = 0
    for i in range(ascii_length):
        j = (j + s[i] + keystream[i % len(keystream)]) % ascii_length
        s[i], s[j] = s[j], s[i]
    return s


def encrypt(plaintext, key):
    i, j = 0, 0
    s = key
    out = []
    for c in plaintext:
        i = (i+1) % ascii_length
        j = (j + s[i]) % ascii_length
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % ascii_length]
        out.append(ord(c) ^ k)
    return ''.join(chr(i) for i in out)


if __name__ == "__main__":
    # lib encryption and decryption
    cipher = ARC4.new("kot")
    encrypted = cipher.encrypt("ala ma kot")
    print("PyCrypto result: {}".format(encrypted))
    cipher = ARC4.new("kot")
    dec = cipher.decrypt(encrypted)
    print(dec)

    # my encryption and decryption
    my_key = create_key("kot")
    my_encrypted = encrypt("ala ma kot", my_key)
    print("MyCrypto result: {}".format(my_encrypted))
    my_key = create_key("kot")
    decryption = encrypt(my_encrypted, my_key)
    print(decryption)
