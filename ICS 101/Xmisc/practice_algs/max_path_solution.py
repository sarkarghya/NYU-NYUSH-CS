#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:46:24 2020

@author: xg7
"""


def maxPath(triangle, all_path=[]):
    current_sums = []
    if len(triangle) == 1:
        return [[0]], [[0]], triangle[0]
    
    ##here is the recursion: we call the maxPath to compute the sums on each node of the last level.
    max_path, all_path, sub_sums = maxPath(triangle[:-1], all_path)
    sub_idx = []
    for i in range(len(triangle[-1])): ##pay attention to the nodes on the most left and most right.
        if i == 0:
            max_v = triangle[-1][0]+sub_sums[0]
            current_sums.append(max_v)
            sub_idx.append(0)
        elif 0 < i < len(triangle[-1])-1:
            if triangle[-1][i]+sub_sums[i-1] >= triangle[-1][i]+sub_sums[i]:
                sub_idx.append(i-1)
                current_sums.append(triangle[-1][i]+sub_sums[i-1])  
            else:
                sub_idx.append(i)
                current_sums.append(triangle[-1][i]+sub_sums[i]) 
        else:  #i == len(triangle[-1])-1
            current_sums.append(triangle[-1][-1]+sub_sums[-1])
            sub_idx.append(i-1)
    all_path.append(sub_idx)
    max_path = pickMaxPath(all_path, current_sums.index(max(current_sums)))
    return max_path, all_path, current_sums


def pickMaxPath(all_path, idx_max_value):
    max_path=[]
    max_path.append(idx_max_value)
    paths = all_path[::-1]
    for path in paths[:-1]:
        max_path.append(path[max_path[-1]])
    return max_path[::-1]


def maxPath_dp(triangle, all_path=[], memo={}):
    #path = []
    current_sums = []
    if len(triangle) == 1:
#        print("root", triangle)
        return [[0]], [[0]], triangle[0]
    try:
        max_path, all_path, sub_sums = memo[len(triangle[:-1])]
    except:
        max_path, all_path, sub_sums = maxPath_dp(triangle[:-1], all_path, memo)
        sub_idx = []
        for i in range(len(triangle[-1])):
            if i == 0:
                max_v = triangle[-1][0]+sub_sums[0]
                current_sums.append(max_v)
                sub_idx.append(0)
            elif 0 < i < len(triangle[-1])-1:
                if triangle[-1][i]+sub_sums[i-1] >= triangle[-1][i]+sub_sums[i]:
                    sub_idx.append(i-1)
                    current_sums.append(triangle[-1][i]+sub_sums[i-1])  
                else:
                    sub_idx.append(i)
                    current_sums.append(triangle[-1][i]+sub_sums[i]) 
            else:  #i == len(triangle[-1])-1
                current_sums.append(triangle[-1][-1]+sub_sums[-1])
                sub_idx.append(i-1)
        all_path.append(sub_idx)
        max_path = pickMaxPath(all_path, current_sums.index(max(current_sums)))
        memo[len(triangle[:-1])] = (max_path, all_path, sub_sums)
    return max_path, all_path, current_sums



if __name__ == "__main__":
    triangle = open("maximum_path_triangle.txt","r").read().split("\n")

    for x in range(len(triangle)):
        triangle[x] = triangle[x].split(" ")
        for y in range(len(triangle[x])):
            triangle[x][y] = int(triangle[x][y])

    for row in triangle:
        print(row)
#    triangle = [[17], [15, 8], [5, 10, 8], [16, 6, 10, 12],[19, 10, 5, 15, 12]]
    max_path, all_path, max_values = maxPath(triangle)
    for row in triangle:
        print(row)
    print()
    print("The maximum path is:{}, the maximum value is:{} ".format(max_path, max(max_values)))
#    print("The maximum path results in: ", maxPath(triangle))
    # Answer is 538 for the test case in triangle.txt
#    print(pickMaxPath(all_path, max_values.index(max(max_values))))

    