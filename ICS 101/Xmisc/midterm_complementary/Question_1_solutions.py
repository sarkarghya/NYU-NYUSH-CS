#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:52:06 2021

@author: bing
"""

def slope(x1, y1, x2, y2):
    if x1 != x2:
        return (y2-y1)/(x2-x1)
    return float("infinity")

##Alternatively
# def slope(x1, y1, x2, y2):
#     try:
#         return (y2-y1)/(x2-x1)
#     except ZeroDivisionError:
#         return float("infinity")


def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    if m != float('infinity'):
        return y1 - m*x1
    return 0


##Testing of your code
if __name__ == "__main__":
    print(slope(1, 1, 2, 2))
    print(intercept(1, 1, 2, 2))
    print(slope(0, 0, 4, 3))
    print(intercept(0, 0, 4, 3))
    print(slope(0, 0, 0, 3))
    print(intercept(0, 0, 0, 3))
    
    