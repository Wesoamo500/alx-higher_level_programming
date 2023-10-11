#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for pos in range(len(my_list)):
        if my_list[pos] == search:
            my_list[pos] = replace
    return my_list
