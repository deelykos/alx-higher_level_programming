#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = len(sys.argv)
    my_sum = 0

    for i in range(1, a):
        my_sum += int(sys.argv[i])
    print(f"{my_sum}")
