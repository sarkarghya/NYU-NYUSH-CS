# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""
import dice_student
import matplotlib.pyplot as plt
import coin_helper

class Block_trial:
    def __init__(self, sides=2, block_size=10):
        self.dice = dice_student.Dice(sides)
        self.block_size = block_size
        self.outcomes = {}
        for i in range(sides):
            self.outcomes[i] = 0
        
    def run(self):
# replace the following line with your code
# roll the dice block_size number of times, recode in 
# the outcome dictionary
        coin_helper.run(self)
    
    def get_run_stats(self):
# report the statistics in a list
# the i-th entry of the list is frequency/percentage 
# the coin lands on the i-th side
        return coin_helper.get_run_stats(self)
        
if __name__ == "__main__":
    a_trial = Block_trial()
    a_trial.run()
    print(a_trial.get_run_stats())
    
    block_size = 100
    total_blocks = 1000
    result = []
    for i in range(total_blocks):
        one_trial = Block_trial(block_size=block_size)
        one_trial.run()
        result.append(one_trial.get_run_stats()[0])

    plt.hist(result)
    plt.title('coin estimate distribution')
    plt.show()
        
    
