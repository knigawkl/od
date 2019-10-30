import sys
import hashlib


def hash_check(n1, n2, howManyBytes):
    h1 = hashlib.sha256(n1.encode()).hexdigest()
    h2 = hashlib.sha256(n2.encode()).hexdigest()
    print(h1[:howManyBytes], h1[howManyBytes:])
    print(h2[:howManyBytes], h2[howManyBytes:])


def match(c, howManyBytes):
    base = {}
    data = f'{c}'
    limit = 200000

    for i in range(1, limit + 1):
        xhash = hashlib.sha256(data.encode()).hexdigest()[:howManyBytes]
        if xhash in base.keys():
            # print(base)
            print('Hash:', xhash, 'Index:', base.get(xhash))
            print('Current index:', i)
            return base.get(xhash), i
        else:
            base[xhash] = i
            data += c
    sys.exit('meh')


char = 'a'
howManyBytes = 8

print('Character:', char, '\nBytes to match:', howManyBytes, '\nGenerating hashes...\n')
n1, n2 = match(char, howManyBytes)

s1 = char * n1
s2 = char * n2

print('\nChecking...')
hash_check(s1, s2, howManyBytes)

with open('plik1.txt', 'w+') as file:
    file.write(s1)

with open('plik2.txt', 'w+') as file:
    file.write(s2)

print('\nStrings saved to plik1 and plik2. Now you can sha256sum plik1.txt plik2.txt')
