#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    x = len(sentence)
    y = sentence[0]
    return (x, y)
