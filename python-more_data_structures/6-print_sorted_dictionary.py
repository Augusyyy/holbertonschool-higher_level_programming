#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = sorted(a_dictionary)
    for k in b_dictionary:
        print("{}: {}".format(k, a_dictionary[k]))
