import time


def fermat(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1


def check(start, end):
    for i in range(start, end):
        res = fermat(i)
        if res:
            print(i)


if __name__ == "__main__":
    start = time.time()
    check(10**60, 10**60+2000)
    print('Took {} seconds'.format(time.time() - start))
