#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:16:23 2019

@author: xg7
"""

# Week 7 Lecture algorithm design workshop demo Q6
# Tiling problem


def tiling(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return tiling(num-1) + tiling(num-2)


##main
num = 5
print("The ways for tiling the 2 x {} board is: {}".format( num, tiling(num)))

