# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""

    
def run(self):
    for i in range(self.num_steps):
        direction = self.dice.roll()
        if direction == 0:
            self.x_pos += 1
        elif direction == 1:
            self.x_pos -= 1
        elif direction == 2:
            self.y_pos += 1
        elif direction == 3:
            self.y_pos -= 1
