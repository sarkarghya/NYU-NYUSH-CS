#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:42:27 2021

@author: bing
"""


    
import sys
def power(x, n):
    """
    Compute x^n, where x, n both are integers.
    :param x: Int -- the base
    :param n: non-negative Int -- the exponent

    :return: Int -- x^n
    """
    if n == 1:
        return x
    if n == 0:
        return 1
        
    if n < 0:
        sys.exit()
    try:
        return x * power(x, n - 1)
    except ZeroDivisionError:
        print('division by zero')


##---Testing ---###
if __name__ == '__main__':
    print(power(4, 3))      # 64
    print(power(-2, 3))     # -8
    print(power(0, 0))      # 1