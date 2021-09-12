#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:56:01 2021

@author: bing
"""

import random
import string



def caesarEncrypt(message, codebook, shift):
    '''
    - you can compute the index of a character, or,
    - you can convert the codebook into a dictionary
    '''
    
    encrypted = ""
    lib = {idx : codebook[(idx + shift)%len(codebook)] for idx in range(len(codebook))}
    for ch in message:
        if ch.isalpha():
            encrypted += lib[codebook.index(ch)]
        else:
            encrypted += ch
    return encrypted


def caesarDecrypt(message, codebook, shift):
    decrypted = ""
    lib = {idx : codebook[(idx - shift)%len(codebook)] for idx in range(len(codebook))}
    for ch in message:
        if ch.isalpha():
            decrypted += lib[codebook.index(ch)]
        else:
            decrypted += ch
    return decrypted


if __name__ == "__main__":
    ##The following several lines generate the codebook
    ##Please don't change it
    random.seed("Caesar")
    
    codebook = []
    for e in string.ascii_letters:
        codebook.append(e)
        
    random.shuffle(codebook)
    print("Your codebook:")
    print(codebook)
    ## end of the codebook generation
    
    m = "Hello Kitty!"
    shift = 3
    encoded = caesarEncrypt(m, codebook, shift)
    decoded = caesarDecrypt(encoded, codebook, shift)
    print("Origin:", m)
    print("Encoded:", encoded)
    print("Decoded:", decoded)