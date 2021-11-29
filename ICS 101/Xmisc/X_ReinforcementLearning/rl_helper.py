# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:01:57 2015

@author: zhengzhang
"""
import random

def get_valid_acts(self, s):
    acts = self.rewards[s]
    valid_acts = []
    for i in range(self.num_acts):
        if acts[i] != -1:
            valid_acts.append(i)
    return valid_acts
    
        
def make_move(self, s, valid_moves):
    if random.random() < self.epsilon:   # explore
        act = random.choice(valid_moves)
    else: # exploit
        act = self.get_maxQ_act(s, valid_moves)      
    return act
    
def update_Q(self, s, a, next_s, r):
    q_star = r + self.gamma * self.get_maxQ(next_s)
    self.set_Q(s, a, q_star)
    return