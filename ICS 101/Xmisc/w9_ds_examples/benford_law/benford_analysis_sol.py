#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:23:22 2021

@author: bing
"""

import os
import math
import pandas as pd
import pickle as pk
import matplotlib.pyplot as plt
from util_sol import Candidate


## data processing
try:
    f = open('US_election_2020.pk', 'rb')
    vote_records = pk.load(f)
    # print('file loaded.')
except FileNotFoundError:
    df = pd.read_csv(os.path.join(os.getcwd(), "w9_ds_examples", "benford_law", "president_county_candidate.csv"))
    vote_records = []
    for i in range(len(df.candidate)):
        vote_records.append(list(df.iloc[i, :]))
    with open(os.path.join(os.getcwd(), "w9_ds_examples", "benford_law", "US_election_2020.pk"), 'wb') as f:
        pk.dump(vote_records, f)


## Beford Analysis
def benford_analysis(candidate):
    numbers = candidate.get_votes().values()
    hist = {i:0 for i in range(1, 10)}
    for n in numbers:
        if n != 0:
            init_n = int(str(n)[0])
            hist[init_n] += 1/len(numbers)
    
    return hist
    

## Plot the result
def plot_result(name, hist):
    benford_distribution = [math.log(1 + 1/i, 10) for i in range(1, 10)]

    fig, ax1 = plt.subplots(1, 1)
    ax1.set_title(name)
    ax1.plot(list(range(1, 10)), benford_distribution, 'g')
    ax1.bar(list(range(1, 10)), list(hist.values()))
    plt.show() # use to show subplots
    
def plot_result2(names, hists):
    benford_distribution = [math.log(1 + 1/i, 10) for i in range(1, 10)]
    fig, axes = plt.subplots(1, len(names))
    c = ('r', 'b', 'g')
    for i in range(len(names)):
        axes[i].set_title(names[i])
        axes[i].plot(list(range(1, 10)), benford_distribution, 'g')
        axes[i].bar(list(range(1, 10)), list(hists[i].values()), color=c[i])
    plt.show() # use to show subplots



if __name__ == "__main__":
    
    biden = Candidate("Joe Biden", vote_records)
    print(benford_analysis(biden))
    hist1 = benford_analysis(biden)
    plot_result(biden.name, hist1)
    trump = Candidate("Donald Trump", vote_records)
    hist2 = benford_analysis(trump)
    plot_result(trump.name, hist2)
    plot_result2([biden.name, trump.name], [hist1, hist2])
    