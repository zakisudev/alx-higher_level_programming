#!/usr/bin/pyhton3
def divisible_by_2(my_list=[]):
    newlist = []
    for n in my_list:
        if n % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return(newlist)
