#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 10:38:18 2021

@author: bing
"""

from itertools import combinations

def count_letters(s):
    return {ch : s.count(ch) for ch in s}


def count_letter_pairs(s, pair_len):
    return {ch : s.count(ch) 
            for ch in [''.join(x) for x in combinations(s, pair_len)] 
            if s.count(ch) > 0}


if __name__ == "__main__":
    s = "banana"
    print(count_letters(s))
    
    s = "banana"
    print(count_letter_pairs(s, 2))
    
    s = "barbarian"
    print(count_letter_pairs(s, 3))
    