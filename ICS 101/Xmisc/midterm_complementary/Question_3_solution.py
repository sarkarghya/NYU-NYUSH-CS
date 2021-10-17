#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:22:25 2020

@author: xianbingu
"""



def maximum(A):
#delete the following line and insert your code
#the built-in max() is not allowed to use here 
    if len(A) <= 1:
        return A[0]
    if A[0] > maximum(A[1:]):
        return A[0]
    else: 
        return maximum(A[1:])





##---test---##
##You can comment out them when you write and test your code.  

if __name__ == "__main__":
    A = [8]
    print(maximum(A))
    A = [3, 2, 5, 7, 9, 10, 2, 4]
    print(maximum(A))
    
