#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:27:55 2020

@author: xg7
"""

##Problem 2
## 2.1
def pick_out_alphabets(s, idxes):
    ##-- You can modify the following code and --## 
    ##-- please insert your code here --##
    output = [] 
    for idx in idxes:
        output.append(s[idx])
    
    ##--your code ends here--##
    return output

## 2.2
def replace_alphabets(s, chars, idxes):
    ##-- You can modify the following code and --## 
    ##-- please insert your code here --##
    output = s
    output = list(output)
    for ch, idx in zip(chars, idxes):
        output[idx] = ch
    output = ''.join(output)    
    ##--your code ends here--##
    return output

## 2.3
def alphabetical_smallest(s, group):
    ##-- You can modify the following code and --## 
    ##-- please insert your code here --##
    output = s
    for idxes in group:
        output = replace_alphabets(output, reversed(pick_out_alphabets(output, idxes)), idxes)
    ##--your code ends here--## 
    return output

        


        
    


if __name__ == "__main__":
    ## test for B1
    print("----Tests for B1----")
    s1 = "helloworld"
    idxes1 = [0, 1, 2, 8] 
    l_str = pick_out_alphabets(s1, idxes1)
    print(l_str)
    idxes2 = [1, 7, 7, 4, 7]
    l_str = pick_out_alphabets(s1, idxes2)
    print(l_str)
    
    ##test for B2
    print("----Tests for B2----")
    s1 = "tears"
    chars1 = ["w", "e", "o", "l"]
    idxes1 = [2, 3, 1, 4]
    new_s1 = replace_alphabets(s1, chars1 , idxes1)
    print(new_s1)
    s2 = "hellokelly"
    chars2 = ["t", "i", "t"]
    idxes2 = [7, 6, 8]
    new_s2 = replace_alphabets(s2, chars2 , idxes2)
    print(new_s2)
    
    ##test for B3
    print("----Tests for B3----")
    s = "gfedcba"
    groups1 = [[0, 1, 2, 3, 4, 5, 6]]
    new_s1 = alphabetical_smallest(s, groups1)
    print(new_s1)
    groups2 = [[0, 1, 2, 3], [5, 6]]
    new_s2 = alphabetical_smallest(s, groups2)
    print(new_s2)
    
    

    