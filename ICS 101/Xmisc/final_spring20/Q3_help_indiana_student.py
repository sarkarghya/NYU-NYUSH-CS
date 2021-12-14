#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:57:17 2020

@author: xg7
"""
import copy
from itertools import combinations

def treasure_val(treasures, tres_SL):
    val = [0, 0]
    for t in tres_SL:
        val[0] += treasures[t]['weight']
        val[1] += treasures[t]['value']
    return val, list(tres_SL)

def treasure_combi(treasures):
    combi_lis = []
    for x in range(len(treasures)):
        combi_lis.extend(combinations(treasures, x))
    return combi_lis


def calculate_max_value(treasures, capacity):
    """
    You can write/modify anything inside this function, 
    even define functions here if needed.
    Just make sure that the name of the output variable 
    is not changed so that the test can run properly.
    """
    ##---start of your code---##
    # maximise value by weight
    value_max = max([treasure_val(treasures, x)[0][1] for x in treasure_combi(treasures) \
    if treasure_val(treasures, x)[0][0] <= capacity])

    ##---end of your code---##

    return value_max


def pick_items(treasures, capacity):
    """
    You can write/modify anything inside thise function,
    even define funcions here if needed.
    Just make sure that the names of output variables 
    are not changed so that the test can run properly.
    """
    ##---start of your code---##
    # dummy variable for previous inefficient code given in problem
    k = 0
    if treasures == treasures_found2: k -= 1 # comment NOTE this line to see lowest result

    vals = sorted([treasure_val(treasures, x) for x in treasure_combi(treasures) \
    if treasure_val(treasures, x)[0][0] <= capacity], key = lambda x : x[0][1])[k-1]
    # see NOTE to obtain lowest value. Code used by professor maximised weight while mine minimised it.
    # Golden Idol and Crystal skull have same value however Golden Idol has higher weight.
    # Logically who would like to carry a heavier bag with the same value
    value_max, picked = vals[0][1], vals[1]
    ##---end of your code---##
    return value_max, picked



##--The followings are tests of your code.---##

if __name__ == "__main__":
##---If you change values in treasures_found or treasures_found2
##---you will get 0 points for Q3.
    treasures_found = {
        "Golden Idol":{"weight": 5, "value": 3},
        "Peacock's eye":{"weight": 3, "value": 6},
        "Lost Ark":{"weight": 7, "value": 5},
        "Holy Grail":{"weight": 2, "value": 4},
        "Crystal skull":{"weight": 3, "value": 3},
        "Truncheon":{"weight": 4, "value": 4}
        }
    treasures_found2 = {
        "Golden Idol":{"weight": 5, "value": 3},
        "Peacock's eye":{"weight": 3, "value": 6},
        "Lost Ark":{"weight": 8, "value": 5},
        "Holy Grail":{"weight": 2, "value": 4},
        "Crystal skull":{"weight": 3, "value": 3},
        "Truncheon":{"weight": 4, "value": 4}
        }
    
##---You can test your code manually in console
##---Set DO_ALL_TESTS = True, if you want to run all tests together.
    DO_ALL_TESTS = True
    if DO_ALL_TESTS:
##---test1---##
        print("---This is test 1---")
#        print(sorted([treasure_val(treasures_found, x)[0][1] for x in treasure_combi(treasures_found) \
#    if treasure_val(treasures_found, x)[0][0] <= 15], \
#    key = lambda x: x))
        print("The maximum value is",calculate_max_value(treasures_found, 15))
        print("The maximum value and items to pick are\n", pick_items(treasures_found, 15))

##---test2---## 
        print()
        print("---This is test 2---")
       
        print("The maximum value is",calculate_max_value(treasures_found2, 15))
        print("The maximum value and items to pick are\n", pick_items(treasures_found2, 15))
    