# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:09:00 2016

@author: zhengzhang
"""

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

print(sorted(mydict.keys())) #sort the keys

for key in sorted(mydict.keys()):
    print("{}: {}".format(key, mydict[key]))

print(sorted(mydict.values())) #sort the values

print(sorted(mydict, key = mydict.get)) #sort the items by values
    
    
    