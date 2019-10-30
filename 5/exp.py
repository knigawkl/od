from multiprocessing import Pool

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

size = 5

arr = bytearray(size)
print(arr)


def f(x):
    return x * x


if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))
