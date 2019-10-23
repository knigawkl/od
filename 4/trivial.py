"""
Przygotuj dwa dokumenty, których funkcje skrótu
trivial_hash() bedą identyczne, a treść różna. Wykorzystaj paradoks urodzinowy.
"""


def trivial_hash(dane):
    hash = 0
    for znak in dane:
        hash += ord(znak)
    return hash % 999


def match_hash(orginal_data, spoofed_data):
    maxTries = 100000000
    hash = trivial_hash(orginal_data)
    for i in range(maxTries):
        if trivial_hash(spoofed_data) == hash:
            print(i)
            return spoofed_data
        spoofed_data = spoofed_data + ' '

    raise RuntimeError(f'Maximum tires excedet - {maxTries}')


ala = 'alamakota'
al2 = ala[::-1]
al3 = 'abecadlozpiecaspaduo'
print(trivial_hash(ala))
print(trivial_hash(al2))

res = match_hash(ala, al3)
print(res)
