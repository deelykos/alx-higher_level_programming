#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    length = len(argv)
if length - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if length == 4:
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print(f"{a} + {b} = {a + b}")
    elif operator == "-":
        print(f"{a} - {b} = {a - b}")
    elif operator == "*":
        print(f"{a} * {b} = {a * b}")
    elif operator == "/":
        print(f"{a} / {b} = {a / b}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
