#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) == 'e' or chr(x) == 'q':
        continue
    print(chr(x).format(x), end='')
