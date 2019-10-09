"""
Napisz algorytm obliczający entropię łańcucha bajtów. Prawdopodobieństwo symboli oblicz
na podstawie ich częstotliwości występowania w łańcuchu.
"""
import math
from a5 import encrypt, create_key

txt = "A complete sentence must have, at minimum, three things: a subject, verb, and an object. The subject is " \
      "typically a noun or a pronoun. And, if there's a subject, there's bound to be a verb because all verbs need a " \
      "subject. Finally, the object of a sentence is the thing that's being acted upon by the subject. "


def entropy(string):
    """Calculates the Shannon entropy of a string"""

    # get probability of chars in string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]

    # calculate the entropy
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])

    return entropy


key = create_key("klucznik")
enc = encrypt(txt, key)


print(entropy(txt))
print(entropy(enc))
