#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:20:20 2021

@author: bing
"""
# def find_farthest_numbers(lst):
#     lst.sort()
#     return lst[0], lst[-1]


def find_farthest_numbers(lst):
    minimum = maximum = lst[0]
    for i in lst[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)



if __name__ == "__main__":
    import random
    random.seed("Midterm")
    
    lst = [i for i in range (100)]
    random.shuffle(lst)
    print("The list:", lst)
    print("The farthest numbers:", find_farthest_numbers(lst))
    