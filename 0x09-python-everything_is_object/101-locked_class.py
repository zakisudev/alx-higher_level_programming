#!/usr/bin/python3
""" Locked class definition """


class LockedClass:
    """ No attritube creation unless first_name  """
    __slots__ = ["first_name"]
