import time
import datetime
import os
os.system("cls")

def countdown(h, m, s):

    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("Time over!")

print("Enter the time (hours-minutes-seconds):")
h, m, s = map(int, input("> ").split('-'))

countdown(h, m, s)
