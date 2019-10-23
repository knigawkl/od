"""
Przy pomocy wywołania bibliotecznej funkcji md5() odtwórz działanie programu md5sum.
"""
from hashlib import md5


def md5sum(file_names):
    result = []
    for file_name in file_names:
        with open(file_name, 'rb') as file:
            hash = md5(file.read()).hexdigest()
            result.append(f'{hash}  {file_name}')
    return '\n'.join(result)


def md5sum_c(checksum_data):
    result = []
    for line in checksum_data.split('\n'):
        hash, file_name = line.split('  ')
        with open(file_name, 'rb') as file:
            data = file.read()
            validation = 'OK' if hash == md5(data).hexdigest() else 'ERROR'
            result.append(f'{file_name}: {validation}')

    return '\n'.join(result)


files = ['a.txt', 'b.txt']
sums = md5sum(files)
print(sums)
print(md5sum_c(sums))
