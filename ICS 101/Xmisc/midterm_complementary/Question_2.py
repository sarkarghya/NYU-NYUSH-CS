#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:05:20 2017

@author: xg7
"""

#Question2
#Q2.1
# l = [1, 1, 2.1, 2.5]
# #l = [1, 1, 1, 2, 2, 2, 1, 1, 1, 2.5]
# d = {1:3, 2:5.5, 6:2.0, 4:2.0}

def remove_non_int(l):
    for e in l[::-1]:
        if type(e) != int:
            l.remove(e)
            
##Alternatively,            
# def remove_non_int(l):
#     for i in range(len(l)-1, -1, -1):
#         if type(l[i]) != int:
#             l.pop(i)
                       

#Q2.2          
def delete_duplicate(l): 
    for i in range(len(l)-1, -1, -1):
        if l[i] in l[:i]:
            l.remove(l[i])

#Q2.3
def do_all(d):
   pass




if __name__ == "__main__":
    print("------testing A1------")
    l1 = [1, 1, 2, 2.5]
    print("l =", l1)
    remove_non_int(l1)
    print("after removing non-int, l =", l1)
    l2 = [1, 1.2, 1.2, 2.5]
    print("l =", l2)
    remove_non_int(l2)
    print("after removing non-int, l =", l2)
    print("------testing A2------")
    l1 = [1, 1, 2, 2.5]
    print("l1 =", l1)
    delete_duplicate(l1)
    print("After deleting duplicates, l =", l1)
    l2 = [1, 0, 1, 1, 0, 2, 2.5]
    print("l2 =", l2)
    delete_duplicate(l2)
    print("After deleting duplicates, l =", l2)
    print("------testing A3------")
    d = {1:3, 2:5.5, 6:2.0, 4:2.0}
    print("d =", d)
    print("After do all, d =", do_all(d))
