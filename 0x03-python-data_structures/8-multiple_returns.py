#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if not sentence:
            return len(sentence), None
        len_str = len(sentence)
        prime = sentence[0]
        return len_str, prime
