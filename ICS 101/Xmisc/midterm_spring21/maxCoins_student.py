#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:27:38 2020

@author: xg7
"""

##Problem 3. Burst ballons
from math import prod

def maxCoins(nums):
    ###---- delete the following lines and insert your code below ----###
    #base case
    if len(nums) == 1:
        return nums[0]
    late_max = 0
    for x in range(len(nums)):
        all_num = nums[:]
        all_num.pop(x)
        sub_max = maxCoins(all_num)
        if x == 0: 
            I_max = sub_max + prod(nums[:x+2])
        elif x == len(nums)-1: 
            I_max = sub_max + prod(nums[x-1:])
        else:
            I_max = sub_max + prod(nums[x-1:x+2])
        if I_max > late_max:
            late_max = I_max
    return late_max

    ###--- end of your code ---###
  

##Bonus
def fast_maxCoins(nums, memo={}):
    ###---- delete the following lines and insert your code below ----###
    if len(nums) == 1:
        return nums[0]
    late_max = 0
    for x in range(len(nums)):
        all_num = nums[:]
        all_num.pop(x)
        try:
            sub_max = memo[(tuple(nums), x)]
        except KeyError:
            sub_max = fast_maxCoins(all_num)
            memo[(tuple(nums), x)] = sub_max #### memory retrival by hashable tuple
        if x == 0: 
            I_max = sub_max + prod(nums[:x+2])
        elif x == len(nums)-1: 
            I_max = sub_max + prod(nums[x-1:])
        else:
            I_max = sub_max + prod(nums[x-1:x+2])
        if I_max > late_max:
            late_max = I_max
    return late_max
    ###--- end of your code ---###



###---Tests of your code.---####
###---When debugging, you can comments them out temporarily if you want.---###
###---But Do not change them.---###
if __name__ == "__main__":
##Tests for maxCoins(). Do not change them.
    print("---testing of your function---")
    nums1 = [3, 1, 5, 8]
    nums2 = [3, 5, 1, 8]
    nums3 = [4, 2, 8, 3, 1, 7]
    print("nums:", nums1)
    coins = maxCoins(nums1)
    print("Max conins:", coins)
    print("nums:", nums2)
    coins = maxCoins(nums2)
    print("Max conins:", coins)
    print("nums:", nums3)
    coins = maxCoins(nums3)
    print("Max conins:", coins)
    print()
##Tests for fast_maxCoins(). Do not change them.    
    print("---testing of the Bonus---")
    nums1 = [3, 1, 5, 8]
    nums2 = [3, 5, 1, 8]
    nums3 = [4, 2, 8, 3, 1, 7]
    print("nums:", nums1)
    coins = fast_maxCoins(nums1)
    print("Max conins:", coins)
    print("nums:", nums2)
    coins = fast_maxCoins(nums2)
    print("Max conins:", coins)
    print("nums:", nums3)
    coins = fast_maxCoins(nums3)
    print("Max conins:", coins)
    