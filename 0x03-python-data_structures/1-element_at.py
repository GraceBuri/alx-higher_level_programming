#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    
    index = 0
    for element in my_list:
        if index == idx:
            return element
        index += 1
    
    return None

