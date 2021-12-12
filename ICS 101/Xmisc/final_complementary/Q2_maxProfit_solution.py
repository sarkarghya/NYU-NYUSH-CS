#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:37:14 2021

@author: bing
"""
import copy


def maxProfit(plist, totalAmount):
    if totalAmount <= 0:
        return 0
    currentMaxP = 0
    if len(plist) == 1: #To avoid the amount always being 0
        for p in plist:
            temp = copy.deepcopy(plist)
            temp.remove(p)
            for amount in range(1, totalAmount+1):#To avoid the amount always being 0
                lastMaxP = maxProfit(temp, totalAmount-amount)
                if lastMaxP+p[amount]>currentMaxP:
                    currentMaxP = lastMaxP + p[amount]
    else:
        for p in plist:
            temp = copy.deepcopy(plist)
            temp.remove(p)
            for amount in range(0, totalAmount+1):
                lastMaxP = maxProfit(temp, totalAmount-amount)
                if lastMaxP+p[amount]>currentMaxP:
                    currentMaxP = lastMaxP + p[amount]
    return currentMaxP
    
            

if __name__ == "__main__":
    plist = [[0, 13, 16, 17, 19], 
              [0, 12, 14, 16, 18],
              [0, 18, 19, 20, 20]]
    amount = 4
    print(maxProfit(plist, amount))