#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:46:40 2021

@author: bing
"""

import copy

## The code only works for lists without repeated elements

def permute(nums, node=[], permutations=[]):
    if len(node)==len(nums):
        permutations.append(node[:])
        return 
    for n in nums:
        if n in node:
            continue
        temp = copy.deepcopy(node)
        temp.append(n)
        permute(nums, temp, permutations)
        
    return permutations


##test
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    p = []
    permute(nums, node=[], permutations=p)
    print("Permutation:", p)
    ## test with repeated elements
    # nums = [1, 1, 3]
    # p1 = permute(nums, [], [])
    # print("Permutation:", p1)
    
    # nums = [4, 1, 2, 3]
    # p2 = permute(nums, [], [])
    # print("Permutation:", p2)
    
    # nums = [4, 1, 1, 4]
    # p3 = permute(nums, [], [])
    # print("Permutation:", p3)

