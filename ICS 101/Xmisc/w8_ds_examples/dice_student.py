# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:23:36 2016

@author: zhengzhang
"""
import random
# import dice_helper

class Dice:
    def __init__(self, sides=2):
        self.n_sides = sides
        self.bounds = [x/sides for x in range(0, sides)]
        self.bounds.append(1)
        self.point = None
        self.lands = 0
   
    def set_bounds(self, r):
        assert len(r) == len(self.bounds) ## if the condition is not satisfied, it stops the program and raises an error
        self.bounds = r
        
    def get_bounds(self):
        return self.bounds
                
    def roll(self):
        self.point = random.uniform(0, 1)       
# replace the following line with you code
# it should set self.point as a random var in [0, 1]
# return which side the dice lands on

        return 0

        # return dice_helper.roll(self)

if __name__ == "__main__":       
    d = Dice(6)
    for i in range(10):
        print("Side-{} is up.".format(d.roll()))
    ''' Let's make a biased dice of 2 sides '''
    d = Dice()
    d.set_bounds([0, 0.3, 1])  
    ones = 0
    num_rolls = 100
    for i in range(num_rolls):
        ones += d.roll()
    print("Biased dice [0, 0.3, 1]:\nThe probability of having side-1 is", ones/float(num_rolls))
    