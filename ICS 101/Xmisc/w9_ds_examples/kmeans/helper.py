# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:31:43 2016

@author: zhengzhang
"""
import sample_student as sample

#### the __sub__ function in sample.py
def __sub__(self, other):
    f = []
    for i in range(self.dimensionality()):
        f.append(self.getFeatures()[i] - other.getFeatures()[i])
    return sample.Sample(self.name + '-' + other.name, f)  

#### the centroid computing function in cluster.py
def computeCentroid(self):
    dim = self.samples[0].dimensionality()
    centroid = sample.Sample('centroid', [0.0]*dim)
    for e in self.samples:
        centroid += e
    centroid /= len(self.samples)
    return centroid

#### the centroid updating function in cluster.py

def update(self, samples):
    oldCentroid = self.centroid
    self.samples = samples
    if len(samples) > 0:
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    else:
        return 0.0

def kmeans_iter(samples, clusters, k):
    #Create a list containing k distinct empty lists
    
    newClusters = []
    for i in range(k):
        newClusters.append([])
    
    #Associate each sample with closest centroid
    for e in samples:
        #Find the centroid closest to e
        smallestDistance = e.distance(clusters[0].getCentroid())
        index = 0
        for i in range(1, k):
            distance = e.distance(clusters[i].getCentroid())
            if distance < smallestDistance:
                smallestDistance = distance
                index = i
        #Add e to the list of samples for the appropriate cluster
        newClusters[index].append(e)
        
    #Update each cluster; check if a centroid has changed
    converged = True
    for i in range(len(clusters)):
        if clusters[i].update(newClusters[i]) > 0.0:
            converged = False
    return converged
 