#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cop_dic = a_dictionary.copy()
    for k, v in cop_dic.items():
        if value == v:
            del a_dictionary[k]
    return a_dictionary
