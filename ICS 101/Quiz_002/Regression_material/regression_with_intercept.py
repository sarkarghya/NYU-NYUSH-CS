#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:12:52 2021

@author: bing
"""


import matplotlib.pyplot as plt
import sample
import optimizer


def compute_error(pred_y, samples):
    n = len(pred_y)
    error = 0
    for i in range(n):
        error += (pred_y[i] - samples[i].getLabel())**2/(2*n)
    return error


def plot_data(samples, pred_y=[]):
    d_x = [s.getFeatures()[0] for s in samples]
    d_y = [s.getLabel() for s in samples]
    plt.cla()
    plt.scatter(d_x, d_y)
    if len(pred_y) > 0:
        plt.plot(d_x, pred_y, 'r')
        title_str = "train error: %0.2f" % error
        plt.title(title_str)
        plt.ylabel('price')
        plt.xlabel('RM')
    plt.show()



f = open('housing_data.txt')

## Loading data
data = f.readlines()
samples = []
for item in data[1:]:
    item = item.strip().split(',')
    features = [float(item[1])]
    label = float(item[0])
    samples.append(sample.Sample("", features, label))

# plot_data(samples)

## Linear regression
error_history = []
w = 5
b = -50
# training loop
parameters = [w, b]
num_iter = 50
steps = 0
margin = 0.01
lr = 0.045
gradient_descent = optimizer.GD(parameters, lr, samples)
VERBOSE = False ##You can set it to True if you want to see the updating process

while True:
    # predict and compute error
    pred_y = [parameters[0] * s.getFeatures()[0] + parameters[1] for s in samples]   
    error = compute_error(pred_y, samples)
    error_history.append(error)
 
    steps += 1
    if error <= margin or steps >= num_iter:
        break
    ## call update to update the parameters by gradient descent
    gradient_descent.update(pred_y)
   
    if VERBOSE:
        plot_data(samples, pred_y)
        
    
##plot the regression line
plot_data(samples, pred_y)
##plot the error history
plt.plot(error_history)
plt.title('training error')
plt.show()


