import fileinput

for line in fileinput.input():
    print(chr(int(line, 16)))
