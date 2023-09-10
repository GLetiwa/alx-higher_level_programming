#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, None)
    x = len(sentence)
    y = sentence[0]
    return (x, y)
