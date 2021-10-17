#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:46:24 2020

@author: xg7
"""


def maxPath(triangle):
    current_sums = []
    if len(triangle) == 1:
        return triangle[0]
    
    ##here is the recursion: we call the maxPath to compute the sums on each node of the last level.
    sub_sums = maxPath(triangle[:-1])
    for i in range(len(triangle[-1])): ##pay attention to the nodes on the most left and most right.
        if i == 0:
            max_v = triangle[-1][0]+sub_sums[0]
            current_sums.append(max_v)
        elif 0 < i < len(triangle[-1])-1:
            if triangle[-1][i]+sub_sums[i-1] >= triangle[-1][i]+sub_sums[i]:
                current_sums.append(triangle[-1][i]+sub_sums[i-1])  
            else:
                current_sums.append(triangle[-1][i]+sub_sums[i]) 
        else:  #i == len(triangle[-1])-1
            current_sums.append(triangle[-1][-1]+sub_sums[-1])

    return current_sums



def maxPath_dp(triangle, memo={}):
    #path = []
    current_sums = []
    if len(triangle) == 1:
#        print("root", triangle)
        return triangle[0]
    try:
        sub_sums = memo[len(triangle[:-1])]
    except:
        sub_sums = maxPath_dp(triangle[:-1], memo)
        for i in range(len(triangle[-1])):
            if i == 0:
                max_v = triangle[-1][0]+sub_sums[0]
                current_sums.append(max_v)
                
            elif 0 < i < len(triangle[-1])-1:
                if triangle[-1][i]+sub_sums[i-1] >= triangle[-1][i]+sub_sums[i]:
                    current_sums.append(triangle[-1][i]+sub_sums[i-1])  
                else:
                    current_sums.append(triangle[-1][i]+sub_sums[i]) 
            else:  #i == len(triangle[-1])-1
                current_sums.append(triangle[-1][-1]+sub_sums[-1])

        memo[len(triangle[:-1])] = sub_sums
    return current_sums



if __name__ == "__main__":
    triangle = open("maximum_path_triangle.txt","r").read().split("\n")

    for x in range(len(triangle)):
        triangle[x] = triangle[x].split(" ")
        for y in range(len(triangle[x])):
            triangle[x][y] = int(triangle[x][y])

    for row in triangle:
        print(row)
#    triangle = [[17], [15, 8], [5, 10, 8], [16, 6, 10, 12],[19, 10, 5, 15, 12]]
    max_values = maxPath(triangle)
    for row in triangle:
        print(row)
    print()
    print("The maximum value is:{} ".format(max(max_values)))
#    print("The maximum path results in: ", maxPath(triangle))
    # Answer is 538 for the test case in triangle.txt
#    print(pickMaxPath(all_path, max_values.index(max(max_values))))

    