"""
Za pomocą analizy statystycznej postaraj się odszyfrować tekst
zaszyfrowany algorytmem przesunięcia cyklicznego o nieznanym kluczu.
"""
import re
from a1 import encrypt

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def analyse_freq(text):
    text = re.sub(r"\s", '', text)
    text = text.upper()
    stat = {}
    for char in text:
        if char in stat:
            stat[char] += 1
        else:
            stat[char] = 1
    stat = sorted(stat, key=stat.get, reverse=True)
    return stat


if __name__ == "__main__":
    with open('texts/written/letters/united1.txt', 'r') as file:
        plaintext = file.read().replace('\n', '')
    with open('texts/written/letters/warner1.txt', 'r') as file:
        plaintext2 = file.read().replace('\n', '')
    print("stats of plaintext letter:")
    plaintext_stats = analyse_freq(plaintext)
    print(plaintext_stats)
    print()
    enc_example = encrypt(1, plaintext2)
    print()
    print("stats of encrypted plaintext2 letter:")
    encrypted_stats = analyse_freq(enc_example)
    print(encrypted_stats)
    print()
    diffs = {}
    for i in range(0, len(plaintext_stats) - 1):
        diff = abs(ord(plaintext_stats[i]) - ord(encrypted_stats[i]))
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    print("Predicted trans length: {}".format(max(diffs, key=diffs.get)))
