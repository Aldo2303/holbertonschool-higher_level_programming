#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    arg_total = len(argv)

    if arg_total == 1:
        print("0 arguments.")
    elif arg_total == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg_total - 1))
        for i in range(1, arg_total):
            print("{}: {}".format(i, argv[i]))
