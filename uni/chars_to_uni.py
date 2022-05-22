import fileinput

for line in fileinput.input():
    print("{0:04X}".format(ord(line.strip('\r\n'))))
