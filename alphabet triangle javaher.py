import string

letters = string.ascii_uppercase

j = 0
for i in range(1, 10, 2):
    print(letters[j:j+i].center(9))
    j += i
