#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:36:15 2020

@author: xg7
"""


##fib recursion
def fib_recursion(n):
    """
    Assum n is an integer n > 0
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_recursion(n-1) + fib_recursion(n-2)


##fib dynamic programming
def fast_fib(n, memo = {}):
    """
    Assume n is an int > 0, memo used only by recursive calls
    returns Fibonacci of n.
    """
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        memo[n] = result
        return result
    

## fib bottom-up
def fib(n):
    """
    n > 0
    This function can return the 
    fib sequence.
    """
#    if n == 1:
#        return 0
    f = [0] * n
#    f = [0 for i in range(n)]
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f



## A more memory saving version:

#def fib(n):
#    """
#    n > 0
#    return the n-th fib number
#    """
#    a = 0
#    b = 1
#    if n == 1:
#        return a
#    if n == 2:
#        return b
#    for i in range(2, n):
#        c = b + a
#        a = b
#        b = c
#    return c




if __name__ == "__main__":
    print(fib(7))    
    print(fib_recursion(7))    




