#!/usr/bin/python3
# 1-my_list.py module
""" Defines Mylist class that inherites from (list) """


class MyList(list):
    """ Defines print_sorted function that returns
    Mylist class attributes in a sorted manner """

    def print_sorted(self):
        """ Process the list attribute and print sorted list """
        print(sorted(self))
