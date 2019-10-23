"""
Korzystając z polecania time sprawdź wydajność dowolnej implementacji algorytmu łamania haseł
metodą brutalnej siły i oszacuj czas maksymalny czas potrzebny do złamania haseł
różnej długości i składający się z małych liter i dużych liter.
"""
import math
import string
import time
from itertools import product

from Crypto.Cipher import ARC4


def calc_entropy(string):
    """Calculates the Shannon entropy of a string"""
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy


def bf(cryptogram, keyLength, keyAlphabet):
    entropyThreshold = 6

    possibleKeys = product(keyAlphabet, repeat=keyLength)
    for k in possibleKeys:
        k = ''.join(k)
        cipher = ARC4.new(k)
        recovered = cipher.decrypt(cryptogram)
        e = calc_entropy(recovered)

        if e < entropyThreshold:
            return k

    return None


if __name__ == "__main__":
    # data = open('a.txt').read()

    data = "A complete sentence must have, at minimum, three things: a subject, verb, and an object. The subject is typically a noun or a pronoun. And, if there's a subject, there's bound to be a verb because all verbs need a subject. Finally, the object of a sentence is the thing that's being acted upon by the subject."
    key = 'abc'
    cipher = ARC4.new(key)
    cryptogram = cipher.encrypt(data)
    res = bf(cryptogram, 3, string.ascii_lowercase)
    print(res)
