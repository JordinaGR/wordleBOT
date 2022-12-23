import itertools
import string
import csv

x = list(string.ascii_lowercase)
x.append('1')

arr = [''.join(p) for p in itertools.product(x, repeat=5)]

with open('diccionari.csv', 'w') as file:
    for i in arr:
        file.write(i + '\n')

