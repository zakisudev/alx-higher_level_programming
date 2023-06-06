#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    new = str[:n] + str[n + 1:]
    return new
