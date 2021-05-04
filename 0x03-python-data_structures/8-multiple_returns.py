#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        first_char = sentence[0]
    else:
        first_char = None
    return (lenght, first_char)
