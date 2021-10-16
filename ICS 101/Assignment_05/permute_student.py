#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:57 2021

@author: bing
"""

def permute(nums):
    #end case
    if len(nums) == 1:
        return [nums]
 
    ls = []
 
    # Iterate the input(nums) and calculate the permutation
    for i in range(len(nums)):
       m = nums[i]
 
       # Extract nums[i] or m from the list.  remnums is
       # remaining list
       remnums = nums[:i] + nums[i+1:] ### please note ###
 
       # Generating all permutations where m is first
       # element
       for p in permute(remnums): ### recursion borrows from future
           ls.append([m] + p)
    return ls
    
##tests

if __name__ == "__main__":
    nums = [1, 2, 3]
    p1 = permute(nums)
    print("Permutation:", p1)
    
    nums = [4, 1, 2, 3]
    p2 = permute(nums)
    print("Permutation:", p2)
    
    nums = [4, 1, 1, 4]
    p3 = permute(nums)
    print("Permutation:", p3)
    

