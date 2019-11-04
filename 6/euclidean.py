def euclid(x, y):
    if x < y:  # We want x >= y
        return euclid(y, x)
    while y != 0:
        (x, y) = (y, x % y)
    return x


def rel_prime(x, y):
    res = euclid(x, y)
    return res == 1


print(euclid(150, 304))
print(euclid(1000, 10))
print(euclid(150, 9))
print(rel_prime(10, 100))
print(rel_prime(6, 35))
