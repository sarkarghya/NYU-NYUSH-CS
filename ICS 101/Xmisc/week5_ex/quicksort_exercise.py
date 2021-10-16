#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:25:10 2021

@author: bing
"""

def quicksort(seq):
    """
    seq is a list of unsorted numbers
    return a sorted list of numbers
    """
    ##stop condition:
    if len(seq) <= 1:
        return seq
    
    ##get the next nodes and process the current node --> call the partition
    else:
        low, pivot, high = partition(seq)
    
    ## self-call to get the sorted left and sorted right
    ## to return the sorted list by concantating the sorted left, pivot, and the sorted right
    return quicksort(low) + [pivot] + quicksort(high)


def partition(seq):
    """
    pick the first element in seq as the pivot
    elements <= pivot goes to the left
    elements > pivot goest to the right
    return the left, pivot, right
    """
    pivot, seq = seq[0], seq[1:] 
    low = [x for x in seq if x <= pivot]
    high = [x for x in seq if x > pivot]
    return low, pivot, high
    


if __name__ == "__main__":
##main

    listA = [9, 7, 6, 4, 2, 7, 8, 13, 1]
    print("Before sorting: ", listA)
    print("After sorting:", quicksort(listA))