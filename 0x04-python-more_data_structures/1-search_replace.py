#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with replaced elements
    result_list = [replace if element == search else element for element in my_list]
    return result_list
