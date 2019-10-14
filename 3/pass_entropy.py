import sys
import string
import random
import math


def calc_entropy(password):
    special = 0
    small = 0
    capital = 0
    digit = 0
    for char in password:
        if ord(char) in range(32, 48):
            special = 1
        if ord(char) in range(48, 58):
            digit = 1
        if ord(char) in range(58, 65):
            special = 1
        if ord(char) in range(65, 91):
            capital = 1
        if ord(char) in range(91, 123):
            small = 1
        else:
            special = 1

    char_pool = 0
    if special == 1:
        char_pool = char_pool + 33
    if small == 1:
        char_pool = char_pool + 26
    if capital == 1:
        char_pool = char_pool + 26
    if digit == 1:
        char_pool = char_pool + 10
    return len(password) * math.log(char_pool, 2)


print("Entropia podanego hasla:")
print(calc_entropy("1234567890"))
