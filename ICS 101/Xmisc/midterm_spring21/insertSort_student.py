#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:13:01 2020

@author: xg7
"""

##Problem 1. insertion sort

import random
random.seed(0)


def insertionSort(lst):
   ###---- delete the following lines and insert your code below ----###
    for i in range (1,len(lst)):
        m=i
        while m>=1 and lst[m]<lst[m-1]:
            lst[m], lst[m-1] = lst[m-1], lst[m]
            m -= 1


   ###--- end of your code ---###


def nInsertionSortOfIdx0(lst, n):
   ###---- delete the following lines and insert your code below ----###
    for i in range(n, len(lst), n):
        m=i
        while m>=n and lst[m]<lst[m-n]:
            lst[m], lst[m-n] = lst[m-n], lst[m]
            m -= n


   ###--- end of your code ---###



###---Tests of your code.---####
###---When debugging, you can comments them out temporarily if you want.---###
###---But Do not change them.---###        
if __name__ == "__main__":
#### test of insertionSort()
    print("-----testing insertionSort()-----")
    lst1 = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    print("Before sorted:\n", lst1)
    insertionSort(lst1)
    print("The result of insertionSort:\n", lst1)
    print()
    lst2 = [random.randint(0, 100) for i in range(10)]
    print("Before sorted:\n", lst2)
    insertionSort(lst2)
    print("The result of insertionSort:\n", lst2)
    print()
### test of nInsertionSortOfIdx0()   
    print("-----testing nInsertionSortOfIdx0()-----")
    lst3 = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    print("Befort sorted:\n", lst3)
    nInsertionSortOfIdx0(lst3, 4)
    print("The result of nInsertionSortOfIdxO with n = 4:\n", lst3)
    print()
    lst4 = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    print("Befort sorted:\n", lst4)
    nInsertionSortOfIdx0(lst4, 6)
    print("The result of nInsertionSortOfIdxO with n = 6:\n", lst4)
            
