#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:30:29 2021

@author: bing
"""


def maximize_A(n, a_num, copy):
    if n <= 0:
        return a_num
    current_A = max(maximize_A(n-1, a_num+1, copy), maximize_A(n-1, a_num+copy, copy), maximize_A(n-2, a_num, a_num))
    
    return current_A

if __name__ == "__main__":
    n = 6
    print(maximize_A(n, 0, 0))
     
    
    