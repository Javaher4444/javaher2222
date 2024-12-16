import os
os.system('cls')

height = int(input("Enter triangle height: "))

def triangle(height):
    for number in range(1, height + 1):
        space = height - number      
        print((space * ' ') + (str(number) * number))

triangle(height)
