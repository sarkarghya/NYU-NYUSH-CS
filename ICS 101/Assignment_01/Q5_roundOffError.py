#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:48:42 2021

@author: bing
"""
import math
def fraction2binary(f, space):
    ##complete the code
    b = ''
    for x in range(space):
        k = math.floor(f*2)
        b += str(k)
        f = f*2 - k 
    return '0.'+b


def binary2fraction(b):
    ##complete the code
    return int(b[2:],2)/2**(len(b)-2)
    

if __name__ =='__main__':
    print('2.07 - 2 =', 2.07 - 2)
    f = 0.07
    l = 52
    print('The binary of 0.07 in your machine:')
    print(fraction2binary(f, l))
    print('Influence of the Truncation error')
    print(binary2fraction(fraction2binary(f, l)))
    
