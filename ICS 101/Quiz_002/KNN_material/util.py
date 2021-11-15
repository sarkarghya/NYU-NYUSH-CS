
import pylab, random
import matplotlib.pyplot as plt
import sample

def plotSamples(samples, marker = 'o', verbose = False):
    xVals, yVals, labels = [], [], []
    for s in samples:
        xVals.append(s.getFeatures()[0])
        yVals.append(s.getFeatures()[1])
        labels.append(int(s.getLabel()))
    plt.scatter(xVals, yVals, c=labels, cmap='Reds')
    plt.xlabel('RM')
    plt.ylabel('DIS')
    cbar = plt.colorbar()
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('Price', rotation=270)
    
    plt.show()


def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    sum = 0
    for i in range(len(v1)):
        sum += (abs(v1[i] - v2[i]) ** p)
    return sum ** (1/p) # helper.minkowskiDist(v1, v2, p)
