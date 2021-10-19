#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:53:44 2020

@author: xg7
"""

##Problem 2. ICSList

import random
random.seed(0)


class ICSList:
    
    
    def __init__(self, l):
   ###---- delete the following lines; insert your code below ----###
          self.data = l
          self.length=len(l)
        
   ###--- end of your code ---###      

    def addItem(self, idx, x):
   ###---- delete the following lines; insert your code below ----###
          if idx > self.length:
               idx = self.length
          self.data.insert(idx,x)
          self.length=len(self.data)
            
   ###--- end of your code ---###
   
    def deleteItem(self, x):
          for i in range(self.length-1,-1,-1):
               if self.data[i]==x:
                    self.data.pop(i)
          self.length=len(self.data)
     
   ###--- end of your code ---###
    
    def len(self):
          return self.length
        
   ###--- end of your code ---###
    
    def _getIncrements(self):
   ###---- delete the following lines; insert your code below ----###
          ret = [1]
          while True:
               le = 3*ret[len(ret)-1] + 1
               if le > self.length:
                    break
               ret.append(le)
          return ret[::-1]

   ###--- end of your code ---###
    
    def _hInsertionSortByIdx(self, idx, h):
   ###---- delete the following lines; insert your code below ----###
          for i in range(h+idx, len(self.data), h):
               m = i
               while m>=h+idx and self.data[m]<self.data[m-h]:
                    self.data[m], self.data[m-h] = self.data[m-h], self.data[m]
                    m -= h
   ###--- end of your code ---###

    def shellSort(self):
   ###---- delete the following lines; insert your code below ----###
          for g in self._getIncrements():
               for h in range(self.length):
                    self._hInsertionSortByIdx(h, g)
          return self.data
   ###--- end of your code ---###




###---Tests of your code.---####
###---When debugging, you can comments them out temporarily if you want.---###
###---But Do not change them.---###
if __name__=="__main__":
    ### test of addItem() ###
    lst = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    print("The example list:\n", lst)
    ml = ICSList(lst)
    print("-----Test of addItem()-----")
    ml.addItem(12, 0)
    print("Testing addItem():\n", ml.data)
    print()
    ### test of deleteItem() ###
    print("-----Test of deletItem()-----")
    lst = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0, 0]
    ml = ICSList(lst)
    print("Before delete 0:\n", ml.data)
    ml.deleteItem(0)
    print("After deleteItem(0):\n",ml.data)
    print("Continue:")
    ml.deleteItem(100)
    print("After deleteItem(100):\n",ml.data)
    print()
    ### test of len() ###
    print("-----Test of len()-----")
    lst = [9, 2, 8, 5, 6, 1, 7, 3]
    ml = ICSList(lst)
    print("Testing the getter of length:\nml.len() returns:", ml.len())
    print()
    ### test of _getIncrements()###
    print("-----Test of _getIncrements()-----")
    ml.length = 20
    print("When length = 20:\n the incretements are", ml._getIncrements())
    ml.length = 10
    print("When length = 10:\n the incretements are", ml._getIncrements())
    print()
    ### test of _hInsertionSortByIdx()###
    print("-----Test of _hInsertionSortByIdx()-----")
    lst1 = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    ml = ICSList(lst1)
    print("Before:\n", ml.data)
    ml._hInsertionSortByIdx(0, 4)
    print("After _hInsertionSortByIdx(0, 4):\n",ml.data)
    ml._hInsertionSortByIdx(1, 4)
    print("Continue:\n After _hInsertionSortByIdx(1, 4)\n", ml.data)
    print()
    ### test of Shell sort ###
    print("-----Test of shellSort()-----")
    lst1 = [9, 2, 0, 8, 5, 6, 1, 7, 3, 0]
    print("Before Shell sort:\n", lst1)
    ml = ICSList(lst1)
    print("After Shell sort:\n", ml.shellSort())
    print()
    lst2 = [random.randint(0, 100) for i in range(30)]
    print("Another test of Shell sort:\nBefore Shell sort:\n", lst2)
    ml = ICSList(lst2)
    print("After Shell sort:\n", ml.shellSort())