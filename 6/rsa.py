# wlasna implementacja generowania kluczy rsa, liczby pierwsze podane
# zaimplementowac liczbe odwrotna modulo, i wzgledne pierwszenstwo
import random


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def mod_inv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b


def euclid(x, y):
    if x < y:  # We want x >= y
        return euclid(y, x)
    while y != 0:
        (x, y) = (y, x % y)
    return x


def rel_prime(x, y):
    res = euclid(x, y)
    return res == 1


def rsa(p, q):
    n = p*q
    euler = (p - 1) * (q - 1)
    """Generating e that is relatively prime to (p-1)*(q-1)"""
    for i in range(2, euler):
        if rel_prime(i, euler):
            e = i
            break
    """Calculate d, the mod inverse of e"""
    d = mod_inv(e, euler)
    private_key = (d, n)
    public_key = (e, n)
    print("private: ", private_key)
    print("public: ", public_key)


if __name__ == "__main__":
    p = 13
    q = 11
    rsa(p, q)
