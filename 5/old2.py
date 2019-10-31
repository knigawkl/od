import hashlib


def create_files(n, m):
    with open('plik1.txt', 'w+') as file:
        file.write('ł' * n)
    with open('plik2.txt', 'w+') as file:
        file.write('ł' * m)


if __name__ == "__main__":
    suffix = 'ł'
    text = suffix
    str_to_hash = {}
    for i in range(1, 100000):
        current_hash = hashlib.sha256(text.encode()).hexdigest()[:8]
        if current_hash in str_to_hash.keys():
            res = str_to_hash.get(current_hash)
            print(i, res)
            create_files(i, res)
            break
        else:
            str_to_hash[current_hash] = i
            text += suffix
