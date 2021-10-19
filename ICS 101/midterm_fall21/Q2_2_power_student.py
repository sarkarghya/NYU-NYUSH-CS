#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:44:01 2021

@author: bing
"""



import sys
def power(x,n):
    """
    Compute x^n, where x, n can both be negative integer.
    :param x: Int -- the base
    :param n: Int -- the exponent

    :return: Int -- x^n
    """
    try:
        if n==0:
            return 1
        elif n==1:
            return x
        elif n>1:
            return x*power(x,n-1)
        elif n<0:
            m=-n
            return 1/(x*power(x,m-1))
            

    except ZeroDivisionError:
        return "Zero division error!"



##---Testing ---###
if __name__ == '__main__':
    print(power(-4, 3))      # -64
    print(power(2, -3))      # 0.125
    print(power(0, -1))      # ZeroDivisionError