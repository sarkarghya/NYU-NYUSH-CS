#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 22:01:38 2021

@author: bing
"""


class GD:
    
    def __init__(self, parameters, lr, samples):
        '''
        parameters: a list, [w, b], the 1st element is w, and the 2nd is b
        lr: learning rate
        samples: a list of samples, each element is an instance of Sample class
        '''
        self.pars = parameters
        self.lr = lr
        self.y = [s.getLabel() for s in samples]
        self.x = [s.getFeatures()[0] for s in samples]
        self.grad_w = 0 ## the gradient of w
        self.grad_b = 0 ## the gradient of b
       
    def compute_grad(self, pred_y):
        '''
        compute the gradient of w and b respectively
        '''
        #cur_y = self.pars[0]*self.pars[1] + self.grad_w 
        n = len(self.y)
        self.grad_w = sum((pred_y[i] - self.y[i]) * self.x[i] for i in range(n))/n
        self.grad_b = sum((pred_y[i] - self.y[i]) for i in range(n))/n
       
    
    def update(self, pred_y):
        '''
        1. compute the gradients of w and b
        2. update self.pars
        '''
        self.compute_grad(pred_y)
        self.pars = [self.grad_w, self.grad_b]
      

