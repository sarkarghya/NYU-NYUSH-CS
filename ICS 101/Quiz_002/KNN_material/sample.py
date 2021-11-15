# -*- coding: utf-8 -*-
import util
NO_NAME_PRINT = False

# Sample class
class Sample(object):
    """
    each instance of the Sample class is one data point in the k-means problem
    """

    def __init__(self, name, features, label = None):
        """
        :param name:
        :param features: an array of numbers. for the 2-d k-means prob, features are the x, y coordinates
               stores in a list [x, y]
        :param label: to store cluster group info
        """
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        return util.minkowskiDist(self.features, other.getFeatures(), 2)

    def setLabel(self, new_label):
        self.label = new_label

    def setName(self, new_name):
        self.label = new_name

    def __add__(self, other):
        """ other is another Sample instance"""
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+', f, self.label)

    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f, self.label)

    def __sub__(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] - other.getFeatures()[i])
        return Sample(self.name + ' - ' + other.name, f, self.label)

    def vec_div(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] / float(other.getFeatures()[i]))
        return Sample(self.name + '/', f, self.label)

    def power(self, x):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] ** (x))
        return Sample(self.name + '-power(' + str(x) + ')', f, self.label)

    def __str__(self):
        return self.name +' , '+ str(self.features) + ' , label: ' + str(self.label)

if __name__ == "__main__":
    a = Sample('a', [1, 1])
    b = Sample('b', [-1, -1])
    c = Sample('c', [10, 10])
    print(a)
    print(b)
    print(a + b)
    print(c - a - b)
    print(a / 2)
    print(b.power(2))
    print(a.dimensionality())
    print(a.getFeatures())
    print(a.distance(b))
