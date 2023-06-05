#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    
    if a > b:
        result = (a * b) + 98
    else:
        result = (a - b) + 98
        
    return result
