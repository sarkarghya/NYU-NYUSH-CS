#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:14:13 2019

@author: xg7
"""

class Bucketsort:
    
    def __init__(self, sizeBucket):
        self.sizeBucket = sizeBucket
        self.buckets = {}
        self.data = None

    
    def _distributeElementsIntoBuckets(self):
        """
        put the elements in the input list into buckects 
        update the self.buckets   
        """
        for item in self.data:
            self.buckets.setdefault(item//10, []).append(item)
    
    
    def sort(self, inputList):
        """
        return the sorted list;
        hint: use the built-in function sorted() to
        sort elements in a bucket
        """
        self.data = inputList
        self._distributeElementsIntoBuckets()
        # not sure if this is how you want us to do
        res = []
        for key in sorted(self.buckets.keys()):
            res.extend(sorted(self.buckets[key]))
        return res
        
        


        
if __name__ == "__main__": 
    ## main 
    import random        
    random.seed(0)
    
    BktSort = Bucketsort(10)
    
    listA = []
    for i in range(100):
        a = random.randint(0,100)
        listA.append(a)
    print(listA)
    listB = BktSort.sort(listA)
    print("SORTED:", listB)    
