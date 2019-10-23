"""
Napisz program korzystający z bazy wygenerowanej przez program htpasswd.
Celem programu jest sprawdzenie, czy użytkownik o podanym identyfikatorze i haśle
jest w pliku bazy.
"""
import string
import sys

# login = sys.argv[2]
# base = open(sys.argv[1])
login = 'adam'
base = open('db')


def znajdz(l, b):
    for line in b.readlines():
        rec = str.split(line, ':')
        if l == rec[0]:
            return True
        else:
            continue
    return False


res = znajdz(login, base)

if res:
    print('W bazie znajduje sie uzytkownik o podanym loginie:', login)
else:
    print('W bazie nie ma uzytkownika o loginie:', login)
