# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 10:58:17 2017

@author: zhengzhang
"""

def compute_error(pred, truth):
    error = 0
    n = len(pred)
    for i in range(n):
        error += (pred[i] - truth[i]) ** 2
    error /= 2*n
    return error

def compute_grad(pred, truth, x):
    n = len(pred)
    grad = sum([(pred[i] - truth[i]) * x[i] for i in range(n)])/n
    return grad