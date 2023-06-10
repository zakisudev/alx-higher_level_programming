#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        first = None
    return (len_str, first)
