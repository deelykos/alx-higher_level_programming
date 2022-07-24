#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    ave = 0
    weig = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            weig += my_list[i][0] * my_list[i][1]
            ave += my_list[i][1]
    return (weig / ave)
