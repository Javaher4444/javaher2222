import os
os.system('cls')

def square(n):
    print(n * '* ')
    for i in range(n-2):
        print('* ' + (n-2) * '  ' + '* ')
    print(n * '* ')

length = int(input('Enter squar side length: '))

if length < 2:
    print('invalid input!')
else:
    square(length)
    