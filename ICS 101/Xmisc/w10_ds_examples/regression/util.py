import random
import sample
import matplotlib.pylab as pylab

LABELS = ('a','b','c')

def genDistribution(xMean=0, xSD=1, yMean=0, ySD=1, n=20, namePrefix=''):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(sample.Sample(namePrefix+str(s), [x, y]))
    return samples

def label(E):
    return E.getLabel()

def make_cmap():
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
    return colors

def make_cmarkers():
    markers = ('o', 'v', '^', '<', '>', '8', 
               's', 'p', '*', 'h', 'H', 'D', 'd')
    return markers

def plot_data(data):
    MARKERS = make_cmarkers()
    COLORS = make_cmap()
    for l in range(len(LABELS)):
        m = MARKERS[l]
        x = [ data[d].getFeatures()[0] for d in range(len(data)) if data[d].getLabel() == LABELS[l] ]
        y = [ data[d].getFeatures()[1] for d in range(len(data)) if data[d].getLabel() == LABELS[l] ]
        pylab.scatter(x,y,label=LABELS[l],marker=m,color=COLORS[l])

    pylab.show()
