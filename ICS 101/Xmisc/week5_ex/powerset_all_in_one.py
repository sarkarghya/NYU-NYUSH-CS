#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:40:33 2020

@author: xg7
"""

from copy import deepcopy


##recursion
def powerset_recursive(lst):
    if len(lst) == 0:
        return [[]]
    pset = powerset_recursive(lst[1:])
    new_subset = deepcopy(pset)
    for subset in new_subset:
        subset.append(lst[0])
    pset.extend(new_subset)
    return pset


##bottom-up
def powerset_add(lst):
    pset = [[]]
    for item in lst:
        new_subset = deepcopy(pset)
        for subset in new_subset:
            subset.append(item)
        pset.extend(new_subset)
    return pset


##combinatorial proof
def powerset_comb(lst):
    pset = []
    total_items = len(lst)
    for i in range(2 ** total_items):
        subset = []
        code = bin(i).split('b')[-1]
#        print(code)
        code = code[::-1]
#        print("inverse:", code)
        for j in range(len(code)):
            if code[j] == '1':
                subset.append(lst[j])
        pset.append(subset)
    return pset
    


if __name__=="__main__":
    
    lst = [1, 3, 5]
    print(powerset_add(lst))
    print(powerset_recursive(lst))
    print(powerset_comb(lst))
    