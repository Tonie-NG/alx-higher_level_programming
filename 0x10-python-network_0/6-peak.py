#!/usr/bin/python3
"""
module for find the oeak in a kist iof unsoted integers.
"""


def find_peak(list_of_integers):
    """peak-finding algorithm"""

    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers)
    if right == 1:
        return list_of_integers[0]
    if right == 2:
        return max(list_of_integers)

    right = right - 1
    while left < right:
        middle = (left + right) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return list_of_integers[left]
