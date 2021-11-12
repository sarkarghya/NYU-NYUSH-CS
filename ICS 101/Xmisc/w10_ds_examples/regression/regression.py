# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:48:26 2017

@author: zhengzhang
"""
import random
import matplotlib.pyplot as plt
import sample
import util

VERBOSE = True

def make_data(n, scale=1):
    """ A simple y = x curve, with noisy displacement on both
        both x and y axis; change scale to change the range
    """
    linear_data = [sample.Sample('', [float(x)/scale, float(x)/scale], '') for x in range(n)]  
    noise = util.genDistribution(xSD=0.3, ySD=0.3, n=n)
    data = [linear_data[i] + noise[i] for i in range(n)]
    return data
    
def compute_error(pred, truth):
    """ mean square error:
        sum of (pred[i] - truth[i])^2, divided by 2*length
    """
    error = 0
    n = len(pred)
    for i in range(n):
        error += (pred[i] - truth[i]) ** 2
    error /= 2*n
    return error

def compute_grad(pred, truth, x):
    """ gradient is mean of (pred[i] - truth[i]) * x[i]
    """
    n = len(pred)
    grad = sum([(pred[i] - truth[i]) * x[i] for i in range(n)])/n
    return grad
    
if __name__ == "__main__":

    num_samples = 100

    # Generating random data
    data = make_data(num_samples, scale=10)
    
    # Make a random split of the data
    random.shuffle(data)
    train_data = data[:80]
    test_data = data[80:]

    # Plotting the randomly generated data
    d_x = [d.getFeatures()[0] for d in train_data]
    d_y = [d.getFeatures()[1] for d in train_data]
#    plt.ion()
    plt.figure(1)
    plt.scatter(d_x, d_y)
    plt.show()
    
    num_iter = 10
    steps = 0
    learning_rate = 0.01
    n = len(train_data)
    error_history = []
    margin = 0.01

    # w is the parameter to be learned
    w = 0.5

    # training loop
    while True:
        
        # predict and compute error
        pred_y = [w*x for x in d_x]   
        error = compute_error(pred_y, d_y)
        error_history.append(error)
        plt.cla()
        plt.scatter(d_x, d_y)
        plt.plot(d_x, pred_y, 'r')
        title_str = "train error: %0.2f" % error
        plt.title(title_str)
        plt.show()
        
        steps += 1
        if error <= margin or steps >= num_iter:
            break
        
        # gradient descent
        grad = compute_grad(pred_y, d_y, d_x)
        w -= learning_rate * grad
        
        if VERBOSE and input("cont? (y/n) ") == 'n':
            break

    # testing on test data
    d_x = [d.getFeatures()[0] for d in test_data]
    d_y = [d.getFeatures()[1] for d in test_data]
    pred_y = [w*x for x in d_x]   
    error = compute_error(pred_y, d_y)
    plt.figure(1)
    plt.scatter(d_x, d_y)
    plt.plot(d_x, pred_y, 'r')
    title_str = "test error: %0.2f" % error
    plt.title(title_str)
    plt.show()
        
    plt.plot(error_history)
    plt.title('training error')
    plt.show()