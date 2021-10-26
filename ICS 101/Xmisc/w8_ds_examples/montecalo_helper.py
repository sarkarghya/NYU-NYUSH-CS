# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""
import math
import random

# compute the Eucliear distance of two vectors
def comp_dist(a, b):
    assert len(a) == len(b)
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return math.sqrt(d)

def estimate_pi(num_points):        
    in_set_x = []
    in_set_y = []
    out_set_x = []
    out_set_y = []
    ins = 0
    
    for i in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if comp_dist([0, 0], [x, y]) < 1.0:
            in_set_x.append(x)
            in_set_y.append(y)
            ins += 1
        else:
            out_set_x.append(x)
            out_set_y.append(y)

    my_pi = 4 * float(ins)/num_points
    return my_pi, in_set_x, in_set_y, out_set_x, out_set_y


        
    