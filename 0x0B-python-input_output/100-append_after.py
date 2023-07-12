#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    words = ""
    with open(filename, encoding="UTF-8") as fr:
        for line in fr:
            words += line
            if search_string in line:
                words += new_string
    with open(filename, "w") as fw:
        fw.write(words)
