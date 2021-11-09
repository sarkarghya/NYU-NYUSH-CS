
#import helper
import pylab, random
import matplotlib.pyplot as plt
import sample
import cluster

LABELS = ('a', 'b', 'c')

def minkowskiDist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    sum = 0
    for i in range(len(v1)):
        sum += (abs(v1[i] - v2[i]) ** p)
    return sum ** (1/p) # helper.minkowskiDist(v1, v2, p)

# generating samples from Gaussian distribution
def genDistribution(xMean=0, xSD=1, yMean=0, ySD=1, n=50, namePrefix='', label = 'a'):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(sample.Sample(namePrefix+str(s), [x, y], label))
    return samples

# plot routines
def plotSamples(samples, marker = 'o', verbose = False):
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
    # plt.show()

def make_cmap():
    colors = ('b', 'g', 'c', 'm', 'y', 'k')
    return colors

def make_cmarkers():
    markers = ('o', 'v', '^', '<', '>', '8',
               's', 'p', '*', 'h', 'H', 'D', 'd')
    return markers
# # MATLAB formatting strings
# def make_cmarkers():
#     markers = ('o', 'v', '^', '<', '>', '8',
#                    's', 'p', '*', 'h', 'H', 'D', 'd')
#     colors = ('b', 'g', 'c', 'm', 'y', 'k')
#     return [c + m for m in markers for c in colors]

def plot_cluster(clusters, verbose = False, centroid = True):
    MARKERS = make_cmarkers()
    COLORS = make_cmap()
    for l in range(len(clusters)):
        c = clusters[l]
        cm = COLORS[l]+ MARKERS[l]
        plotSamples(c.getMembers(), cm, verbose)
        if centroid:
            plotSamples([c.centroid], 'sr')
    plt.show()



if __name__ == "__main__":

    #print(minkowskiDist([0, 0], [1, 1], 1))
    #print(minkowskiDist([0, 0], [1, 1], 2))

    test_samples = genDistribution()
    c = cluster.Cluster(test_samples)
    plot_cluster([c])


    # plotSamples(test_samples, 'o')
    # plotSamples([test_samples[0]], 'sk')
    # plt.show()
