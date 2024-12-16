from time import sleep

count = 1
width = 20

for i in range(10):
    print(("*" * count).center(width))
    count += 2
    sleep(0.5)
print("| |".center(width))

print("Happy New Year".center(width))
print("2025".center(width))
