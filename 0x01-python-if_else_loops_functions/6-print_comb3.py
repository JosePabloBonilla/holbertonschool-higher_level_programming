#!/usr/bin/python3
for i in range(89):
    if i / 10 < i % 10:
        print('{:02}'.format(i), end=', ')
i = 89
print('{:02}'.format(i))
