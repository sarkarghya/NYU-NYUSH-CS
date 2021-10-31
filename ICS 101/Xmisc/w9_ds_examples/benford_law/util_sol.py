#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:13:58 2021

@author: bing
"""
    
    
class Candidate:
    #start
    def __init__(self, name, vote_records):
        self.name = name
        self.votes = self.count_vote(vote_records)
        
    def count_vote(self, vote_records):
        votes = {}
        for rec in vote_records:
            if rec[2] == self.name:        
                votes[(rec[0], rec[1])] = rec[4]
        return votes
        
    def get_name(self):
        return self.name
    
    def get_votes(self):
        return self.votes
    #end
    
if __name__ == "__main__":
    ## data processing
    import pandas as pd
    import pickle as pk
    try:
        f = open('US_election_2020.pk', 'rb')
        vote_records = pk.load(f)
        # print('file loaded.')
    except FileNotFoundError:
        df = pd.read_csv('president_county_candidate.csv')
        vote_records = []
    
        for i in range(len(df.candidate)):
            vote_records.append(list(df.iloc[i, :]))
            
        
        f = open('US_election_2020.pk', 'wb')
        pk.dump(vote_records, f)
        f.close()
    
    biden = Candidate("Joe Biden", vote_records)
    print(biden.get_name())
    print(biden.get_votes())
    