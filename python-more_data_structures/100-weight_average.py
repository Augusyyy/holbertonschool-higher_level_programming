#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    total_weight = 0
    number = 0
    for tup in my_list:
        total_weight += (tup[0] * tup[1])
        number += tup[1]
    return (total_weight / number)
