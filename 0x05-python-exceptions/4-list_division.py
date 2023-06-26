#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    ans = 0
    for i in range(list_length):
        try:
            ans = my_list[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("Division by 0")
            continue
        except TypeError:
            print("Wrong Type")
            continue
        except IndexError:
            ans = 0
            print("Out of Range")
            continue
        finally:
            newList.append(ans)
    return (newList)
