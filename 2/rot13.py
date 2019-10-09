import fileinput

table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

for line in fileinput.input():
    line = line.rstrip()
    print(str.translate(line, table))
