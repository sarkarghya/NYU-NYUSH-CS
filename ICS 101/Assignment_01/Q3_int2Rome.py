#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:50:19 2020

@author: xg7
"""

def convert_to_Roman_numeral(A):
#    can be improved
    rome_dict = {(2**(num//2))*(5**(num//2 + num%2)): lett for num, lett in enumerate('IVXLCDMGH')}

    res = ''
    for num, ln in enumerate(map(int, str(A)), 1):
        div = 10**(len(str(A)) - num)
        k = ln//5
        ln %= 5
        if ln <= 3:
            res += (rome_dict[div*5]*k + rome_dict[div] * ln)
        else:
            res += (rome_dict[div] + rome_dict[div*5*k])
    return res
    
##test
if __name__ == "__main__":
    n = 1800
    print(convert_to_Roman_numeral(n))
