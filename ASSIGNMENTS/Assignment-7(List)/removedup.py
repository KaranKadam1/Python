# write a python program to remove duplicate element from a list

from typing import final


def removeDup(l1):

    final_list = []

    for x in l1:
        if x not in final_list:
            final_list.append(x)

    return final_list

l1 = [2,4,10,20,5,2,20,4]
print(removeDup(l1))


