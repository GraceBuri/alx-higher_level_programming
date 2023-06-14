#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()

    for key in new_dir:
        new_dir[key] *= 2

    return new_dir
