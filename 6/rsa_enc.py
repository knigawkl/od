"""
Otrzymujesz od adresata klucz publiczny w postaci pary liczb (e, n).
Wiadomość do zaszyfrowania zamieniasz na liczby naturalne t, które muszą spełniać nierówność 0 < t < n
Na tak otrzymanych liczbach wykonujesz operację szyfrowania i otrzymujesz liczby c = t^e mod n.
Liczby c są zaszyfrowaną postacią liczb t i przekazuje się je adresatowi wiadomości.
Klucz (e, n) umożliwił ich zaszyfrowanie, lecz nie pozwala ich rozszyfrować.
"""


def text_to_digits(txt: str):
    res = ''
    for i in txt:
        res += str(ord(i) - 65)
    return res


def digits_to_text(digits):
    res = ''
    num = [int(x) for x in str(digits)]
    for i in range(0, len(num) - 1, 2):
        units = num[i + 1]
        tens = num[i]
        asc = 10 * tens + units
        res += chr(asc + 65)
    return res


def rsa_enc(e, n, msg: int):
    enc = (msg ** e) % n
    print('Encrypted message: ', enc)
    return enc


def rsa_dec(d, n, enc: int):
    dec = (enc ** d) % n
    print('Decrypted message: ', dec)
    return dec


msg = text_to_digits("a")
print("msg as number: ", msg)
enc = rsa_enc(7, 143, msg=int(msg))
dec = rsa_dec(103, 143, enc=enc)
res = digits_to_text(dec)
print("Result: ", res)
# wiadomosc t bedaca liczba musi spelniac 0<t<n