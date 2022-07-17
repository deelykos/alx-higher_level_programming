#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):  # iteration for rows
        for j in range(len(matrix[i])):  # iteration for the items in the row
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):  # $ will have no space
                print(" ", end="")

        print("")
