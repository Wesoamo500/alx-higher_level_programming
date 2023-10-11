#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for pos in range(len(my_list)):
        if my_list[pos] == search:
            new_list[pos] = replace
        else:
            new_list[pos] = my_list[pos]
    return new_list
