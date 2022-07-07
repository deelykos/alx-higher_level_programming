#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    a = len(sys.argv)
    argument = a - 1

    if argument == 0:
        print("0 arguments.")

    elif argument == 1:
        print("1 argument:\n1: {:s}".format(sys.argv[1]))

    else:
        print("{:d} arguments:".format(argument))
        for i in range(1, a):
            print("{:d}: {:s}".format(i, sys.argv[i]))
