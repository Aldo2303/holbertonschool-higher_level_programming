#!/usr/bin/python3
for num in range(90):
    if num != 89 and num / 10 < num % 10:
        print("{:02}".format(num), end=', ')
    elif num == 89:
        print("{:02}".format(num))
    