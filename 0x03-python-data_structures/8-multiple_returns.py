#!/usr/bin/python3
def print_sorted_list(my_list=[]):
    sorted_list = sorted(my_list)
    for i in map(str, sorted_list):
        print(i)

