# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 10:13:16 2014

@author: zzhang
"""
import random
import pickle

class Roman2num:
    def __init__(self, fname):
        self.int2roman = {}
        self.roman2int = {}
        self.fname = fname
        self.outfname = fname + '.pk'
        
    def build_table(self):
        self.f = open(self.fname, 'r')
        lines = self.f.readlines()
        for t in lines:
            items = t.split(':')
            items = [x.strip() for x in items]
            rank = int(items[0])
            roman_numeral = items[1]
            self.int2roman[rank] = roman_numeral
            self.roman2int[roman_numeral] = rank
        self.f.close()
        
    def write_table(self):
        self.outf = open(self.outfname, 'wb')
        pickle.dump(self.int2roman, self.outf)
        pickle.dump(self.roman2int, self.outf)
        self.outf.close()
        
if __name__ == "__main__":
    r = Roman2num('roman.txt')
    r.build_table()
    
    for i in range(10):
        x = random.randint(0, 20) + 1
        s = r.int2roman[x]
        print(x, s)
        
    r.write_table()
    

                
            