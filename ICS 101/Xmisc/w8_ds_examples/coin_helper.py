# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""
import dice_student

def run(self):
    for i in range(self.block_size):
        self.outcomes[self.dice.roll()] += 1

def get_run_stats(self):
    stats = []
    for k in sorted(self.outcomes):
        stats.append(self.outcomes[k]/float(self.block_size))
    return stats
        

        
    