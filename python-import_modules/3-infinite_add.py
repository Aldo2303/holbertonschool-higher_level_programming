#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    sum = 0
    argv_total = len(argv)

    for i in range(1, argv_total):
        sum += int(argv[i])
    print("{}".format(sum))
