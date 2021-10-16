#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:41:35 2020

@author: xg7
"""




def minBills(bills, value):
    if value == 0:
        return [], 0
    num = float("inf") 
    for b in bills:
        if b <= value:
            p, sub_num = minBills(bills, value-b)
            if sub_num + 1 < num:
                num = sub_num + 1 
                pk = p + [b]
    return pk, num



def fast_minBills(bills, value, memo={}):
    if value == 0:
        return [], 0
    num = float("inf") 
    for b in bills:
        if b <= value:
            try:
                p, sub_num = memo[(b, value-b)]
            except KeyError:
                p, sub_num = fast_minBills(bills, value-b, memo)
                memo[(b, value-b)] = (p, sub_num)
            if sub_num + 1 < num:
                num = sub_num + 1 
                pk = p + [b]
    return pk, num



if __name__ == "__main__":
    
    bills = [9, 6, 5, 1]
    value = 11
    picked, n = minBills(bills, value) 
    print(picked, n)
    
    bills2 = [100, 50, 20, 10, 5, 2, 1]
    value2 = 123
    picked2, n2 = fast_minBills(bills2, value2) 
    print(picked2, n2)
    
   