# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:14:38 2016

@author: zhengzhang
"""
#import dice_student
import math
import matplotlib.pyplot as plt
import random

# compute the Eucliear distance of two vectors
def comp_dist(a, b):
    assert len(a) == len(b)
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i]) ** 2
    return math.sqrt(d)

# use math.uniform(-1, 1) twice to get cordinate of a random dot
# record how many times dots are within unit circle
# should return:
# - an estimate of pi
# - the x-axis cordinates list for those within the unit circle
# - the y-axis cordinates list for those within the unit circle
# - the x-axis cordinates list for those outside the unit circle
# - the y-axis cordinates list for those outside the unit circle
def estimate_pi(num_points):        
    in_set_x = []
    in_set_y = []
    out_set_x = []
    out_set_y = []
    ins = 0
    
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if comp_dist([0, 0], [x, y]) < 1.0:
            in_set_x.append(x)
            in_set_y.append(y)
            ins += 1
        else:
            out_set_x.append(x)
            out_set_y.append(y)

    my_pi = 4 * float(ins)/num_points #from emperical probability of pi i.e. my_pi/4 = ins/num_points
    return my_pi, in_set_x, in_set_y, out_set_x, out_set_y

results = []
# total number of random dots per trial
num_points_per_estimate = 1000
# perform multiple trails
num_trials = 100
for _ in range(num_trials):
    est_pi, in_x, in_y, out_x, out_y = estimate_pi(num_points_per_estimate)
    results.append(est_pi)

print("estimated pi: ", sum(results)/num_trials)

# visualize the dots in the last trial
plt.subplot(2, 1, 1)
plt.title('dots distribution')
plt.scatter(in_x, in_y, c='r')
plt.scatter(out_x, out_y, c='b')

# visualize the estimations of all trials
plt.subplot(2, 1, 2)
plt.title('estimate of pi')
plt.hist(results)

plt.show()
        
    