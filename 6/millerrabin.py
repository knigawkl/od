import time
from random import randrange
from pygments.util import xrange


def is_prime(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def miller(start, end):
    for i in range(start, end):
        res = is_prime(i)
        if res:
            print(i)


if __name__ == "__main__":
    start = time.time()
    miller(10**60, 10**60+2000)
    print('Took {} seconds'.format(time.time() - start))
