# import os
# os.system('cls')

height = int(input('Enter height: '))

def triangle(h):

    for i in range(1, (2 * h + 1), 2):
        print(('*' * i).center(2 * h + 1))

triangle(height)
