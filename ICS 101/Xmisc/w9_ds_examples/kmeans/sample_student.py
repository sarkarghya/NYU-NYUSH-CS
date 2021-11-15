# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:36:11 2015

@author: zhengzhang
"""
import util
import helper

# Sample class
class Sample(object):
    
    def __init__(self, name, features, label = None):
        #Assumes features is an array of numbers
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
        
    def __add__(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+' + other.name, f)        
        
    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f)

    #### Implement an overwrite of the '-' operator here!
    def __sub__(self, other):
        ''' replace the line below with you code
            refer to the __add__ for ideas '''
        #return helper.__sub__(self, other)
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] - other.getFeatures()[i])
        return Sample(self.name + '-' + other.name, f) 
    
    def __mul__(self, other):
        ''' bonus: can you do vector multiplication?
            this is two vectors element-wise multiplication '''
        pass
        
    def __str__(self):
        return self.name +':'+ str(self.features) + ':' + str(self.label)

if __name__ == "__main__":
    a = Sample('a', [1, 1])
    b = Sample('b', [-1, -1])
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a/2)

