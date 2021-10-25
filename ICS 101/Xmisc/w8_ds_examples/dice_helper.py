# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:23:36 2016

@author: zhengzhang
"""
import random
def roll(self):
    self.point = random.uniform(0, 1)
    for i in range(self.n_sides):
        if self.point > self.bounds[i] \
        and self.point <= self.bounds[i+1]:
            break
    self.lands = i
    return self.lands

