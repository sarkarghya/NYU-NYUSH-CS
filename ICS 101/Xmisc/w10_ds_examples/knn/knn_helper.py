# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:52:09 2016

@author: zhengzhang
"""
import util

def knn(p, data, k): 
    # Calculating the distances b/w p & every pt. in data
    distances = {}
    for d in data:
        if d.distance(p) not in distances.keys():
            distances[ d.distance(p) ] = [ d ]
        else:
            distances[ d.distance(p) ].append(d)

    # Sorting the k nearest neighbours
    result = []        
    for key in sorted(distances.keys()):
        result.extend( distances[key] )

    k_nearest_neighbours = result[:k]

    # Assigning a label to the new point based on the k neighbours
    label_votes = { l:0 for l in util.LABELS }
    for x in k_nearest_neighbours:
        label_votes[x.getLabel()] += 1
    max_label = sorted(label_votes, key = label_votes.get, reverse = True)[0]
    
#    max_vote = 0
#    for k , v in label_votes.items():
#        if v > max_vote:
#            max_label = k
    p.setLabel(max_label)
