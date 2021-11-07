#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:57:17 2020

@author: xg7
"""
import copy



def calculate_max_value(treasures, capacity):
    """
    You can write/modify anything inside this function, 
    even define functions here if needed.
    Just make sure that the name of the output variable 
    is not changed so that the test can run properly.
    """
    ##---start of your code---##
    
    value_max = 0
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
    value_max = 0
    picked = []
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
        
        print("The maximum value is",calculate_max_value(treasures_found, 15))
        print("The maximum value and items to pick are\n", pick_items(treasures_found, 15))

##---test2---## 
        print()
        print("---This is test 2---")
       
        print("The maximum value is",calculate_max_value(treasures_found2, 15))
        print("The maximum value and items to pick are\n", pick_items(treasures_found2, 15))
    