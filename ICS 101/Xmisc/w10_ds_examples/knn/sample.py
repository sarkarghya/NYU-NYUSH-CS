# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:16:01 2016

@author: zhengzhang
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:36:11 2015

@author: zhengzhang
"""

class Sample(object):
    
    def __init__(self, name, features, label=None):
        #Assumes features is an array of numbers
        self.name = name
        self.features = features
        self.label = label
        
    def getDimensionality(self):
        return len(self.features)
    
    def getFeatures(self):
        return self.features[:]
    
    def getLabel(self):
        return self.label
        
    def setLabel(self, label):
        self.label = label
    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
    
    def distance(self, other):

        def minkowskiDist(v1, v2, p=2):
            """Assumes v1 and v2 are equal-length arrays of numbers
               Returns Minkowski distance of order p between v1 and v2"""
            dist = 0.0
            for i in range(len(v1)):
                dist += abs(v1[i] - v2[i])**p
            return dist**(1.0/p)
            
        return minkowskiDist(self.features, other.getFeatures())
        
    def __add__(self, other):
        f = []
        for i in range(self.getDimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+' + other.name, f, self.label)        
        
    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f)

    def __sub__(self, other):
        f = []
        for i in range(self.getDimensionality()):
            f.append(self.getFeatures()[i] - other.getFeatures()[i])
        return Sample(self.name + '-' + other.name, f)   
    
    def __str__(self):
        return self.name +': ' \
            + str(self.features) + ': ' \
            + str(self.label)

if __name__ == "__main__":
    x = Sample('x', [1, 2])
    y = Sample('y', [4, 5])
    print(x + y)
    print(x - y)
    print(x / 4)
    pass