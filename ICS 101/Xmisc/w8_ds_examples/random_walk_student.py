# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""
import dice_student
import math
import matplotlib.pyplot as plt

import random_walk_helper

class Walker:
    def __init__(self, directions=4, num_steps=10):
        self.dice = dice_student.Dice(directions)
        self.num_steps = num_steps
        self.x_pos = 0
        self.y_pos = 0
        
    def set_bounds(self, r):
        self.dice.set_bounds(r)
        
    def run(self):
# replace the following line with you code
# roll the dice, according to the outcome:
# - go left one step (x -= 1)
# - go right one step (x += 1)
# - go north one step (y += 1)
# - go south one step (y -= 1)
        random_walk_helper.run(self)
    
    def get_position(self):
        return self.x_pos, self.y_pos
        
    def get_dist(self):
        
        def comp_dist(a, b):
            assert len(a) == len(b)
            d = 0
            for i in range(len(a)):
                d += (a[i] - b[i]) ** 2
            return math.sqrt(d)
            
        return comp_dist([0, 0], [self.x_pos, self.y_pos])
        
if __name__ == "__main__":
    one_walker = Walker()
    one_walker.run()
    print("one walk", one_walker.get_dist())
    
    num_steps = 100
    total_walks = 2000
    result = []
    x_pos_list = []
    y_pos_list = []
    
    weights = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    for i in range(total_walks):
        one_walker = Walker(num_steps=num_steps)
        one_walker.set_bounds(weights)
        one_walker.run()
        x, y = one_walker.get_position()
        x_pos_list.append(x)
        y_pos_list.append(y)
        result.append(one_walker.get_dist())
    
    print("mean distance:", sum(result)/total_walks)
    plt.subplot(2, 1, 1)
    plt.hist(result)
    plt.title('position distribution')
    
    plt.subplot(2, 1, 2)
    plt.title('2D distribution')
    plt.scatter(x_pos_list, y_pos_list)
    
    plt.show()
    