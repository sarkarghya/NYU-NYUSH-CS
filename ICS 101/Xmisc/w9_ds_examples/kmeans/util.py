# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:36:11 2015

@author: zhengzhang
"""

#import pylab, random
import random
import matplotlib.pyplot as plt
import sample_student as sample

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)

# generating samples from Gaussian distribution
def genDistribution(xMean=0, xSD=1, yMean=0, ySD=1, n=50, namePrefix=''):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(sample.Sample(namePrefix+str(s), [x, y]))
    return samples

# plot routines
def plotSamples(samples, marker='o', verbose = False):
    xVals, yVals = [], []
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
        if verbose:
            pylab.annotate(s.getName(), xy = (x, y),
                           xytext = (x+0.13, y-0.07),
                           fontsize = 'x-large')
        xVals.append(x)
        yVals.append(y)
    plt.plot(xVals, yVals, marker)

# MATLAB formatting strings
def make_cmarkers():
    markers = ('o', 'v', '^', '<', '>', '8', 
                   's', 'p', '*', 'h', 'H', 'D', 'd')
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
    return [c + m for m in markers for c in colors]

def plot_cluster(clusters, verbose = False):
    color_markers = iter(make_cmarkers())
    for c in clusters:
        cm = next(color_markers)
        plotSamples(c.getMembers(), cm, verbose)
        plotSamples([c.centroid], 'sk')
    plt.show()

if __name__ == "__main__":
    
    print(minkowskiDist([0, 0], [1, 1], 1))
    print(minkowskiDist([0, 0], [1, 1], 2))
    
    test_samples = genDistribution()
    plotSamples(test_samples, 'o')