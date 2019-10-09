import string
import sys
import fileinput


def encrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result


res = encrypt(2, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(res)

'''
# trans_length = int(sys.argv[1])
trans_length = 28
while trans_length > 25:
    trans_length = trans_length % 26

plaintext = "abcdefghijklmnopqrstuvwxyz"
translation = "%s%s" % (plaintext[trans_length:26], plaintext[0:trans_length])
print("plaintext:   %s" % plaintext)
print("translation: %s" % translation)
print("trans length equal to: {}".format(trans_length))

table = str.maketrans(plaintext, translation)
for line in fileinput.input(sys.argv[1]):
        line = line.rstrip()
        print(str.translate(line, table))
'''
