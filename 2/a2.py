"""
Napisz program szyfrujący algorytmem Vigenere. Założenia odnośnie do alfabetu jak w 1.
"""
ascii_length = 256


def generateKeystream(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return key
    if len(plaintext) < len(key):
        return key[:len(plaintext)]
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt(plaintext, key):
    cipher_text = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % ascii_length
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + ascii_length) % ascii_length
        orig_text.append(chr(x))
    return "".join(orig_text)


if __name__ == "__main__":
    plaintext = "ÍÑÎÜÏ×ÔáÐ"
    key = "lemon"
    keystream = generateKeystream(plaintext, key)
    cipher = encrypt(plaintext, keystream)
    check = decrypt(cipher, keystream)
    print("Cipher:   ", cipher)
    print("Plaintext:", check)
