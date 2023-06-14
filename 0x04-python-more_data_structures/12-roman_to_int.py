#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_to_int(roman_string):
        return (0)
    rom = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500,'M' : 100}
    con = 0
    for x in range(len(roman_string)):
        if x > 0 and rom[roman_string[x]] > rom[roman_string[x - 1]]:
            con += rom[roman_string[x]] - 2 * rom[roman_string[x - 1]]
        else:
            con += rom[roman_string[i]]
    return con
