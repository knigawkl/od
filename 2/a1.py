"""
Napisz program szyfrujący algorytmem przesunięcia cyklicznego o wybraną liczbę.
Jako alfabet proszę założyć dowolny znak, którego kod znajduje się w przedziale <0, 255>.
Przydatne funkcje w Python to chr(kod) i ord(znak).
The chr() function takes an integer ordinal and returns a single-character string.
The ord() function takes a single-character string, and returns the integer ordinal value.
"""


def encrypt(key, plaintext):
    """dua dak"""
    alpha = ""
    for i in range(0, 255):
        appendix = chr(i)
        alpha = "{}{}".format(alpha, appendix)
    result = ""
    for letter in plaintext:
        if letter in alpha:
            letter_index = (ord(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result


if __name__ == "__main__":
    step = 3
    text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    print("plaintext:  {}".format(text))
    print("cipher:     {}".format(encrypt(step, text)))
    print("dedcrypted: {}".format(encrypt(-step, encrypt(step, text))))

