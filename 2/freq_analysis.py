import re
import sys

stat = {}
# press ^d to send an EOF
for line in sys.stdin.readlines():
    line = re.sub(r'\s', '', line)
    # matches a space character (space, \t, \r (carriage return), \n)
    for char in line:
        if char in stat:
            stat[char] += 1
        else:
            stat[char] = 1
for char in sorted(stat, key=stat.get, reverse=True):
    print("{} <=> {}".format(char, stat[char]))
