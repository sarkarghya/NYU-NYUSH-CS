#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:48:59 2020

@author: xg7
"""

import string

def lenLastWord(s):
    return len(''.join([ch for ch in s if ch not in string.punctuation]).split().pop())


##test
if __name__ == "__main__":
    
    s = "hello world."
    print(lenLastWord(s))
    
    s = "Good morning  !"
    print(lenLastWord(s))
   
