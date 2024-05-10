#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError, IndexError):
            pass
        else:
            ret += 1
    print()
    return (ret)

my_list = [1, 2, 3, 4]
ret = safe_print_list_integers(my_list,len(my_list) + 4)
print(ret)
