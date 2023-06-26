#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    ans = 0
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
            continue
        except TypeError:
            print("wrong type")
            ans = 0
            continue
        except IndexError:
            ans = 0
            print("out of range")
            continue
        finally:
            newList.append(ans)
    return (newList)
