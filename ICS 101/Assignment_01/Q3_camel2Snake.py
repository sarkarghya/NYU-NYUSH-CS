#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:43:58 2020

@author: xg7
"""

def camel2snake():
    st = input('Please input a camel: ')
    result = ''
    for char in st:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    return result

print(camel2snake())