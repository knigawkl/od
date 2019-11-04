from math import sqrt


def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step


# check if num is prime
def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))


def check(start, end):
    for i in range(start, end):
        res = is_prime(i)
        if res:
            print(i)


if __name__ == "__main__":
    check(10**60, 10**61)
