#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        result = (sen_len, None)
    else:
        result = (sen_len, sentence[0])

    return result
