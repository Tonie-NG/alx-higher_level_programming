#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    if len(sen_len) == 0:
        return None
    return ("Length: {} - First character: {}".format(sen_len, sentence[0]))
