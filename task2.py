import os, sys
from random import choice

list = []

def list_ran():
    if len(sys.argv) > 3:
        for i in range (2, len(sys.argv)):
            list.append(sys.argv[i])
        print('Последовательность: ', list)
        print('Случайный элемент:', choice(list))
    elif len(sys.argv) == 3:
        print('Мало элементов')
    elif len(sys.argv) < 3:
        print('None')

command = sys.argv[1]
if command == 'write':
    list_ran()
else:
    print(' ')