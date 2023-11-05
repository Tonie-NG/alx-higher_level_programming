#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for i in range(0, len(my_list)):
        val = my_list[i]
        if val % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result

