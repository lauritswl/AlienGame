# -*- coding: utf-8 -*-

import glob
#import os
import random
import pandas as pd
import numpy as np

# change directory to stimulus folder
#os.chdir('/Users/au155600/Dropbox/Monster_exp/Exp setup/MonsterExp2.0/AlienGameCode/pictures/')

training = glob.glob('[0-9]*.png')
print(training)
# prepare pandas data frame for recorded data
columns = ['sequence1', 'sequence2', 'sequence3', 'sequence4', 'sequence5']
STIMULI = pd.DataFrame(columns=columns, index = range(320))

#STIMULI['block'] = ['training'] * 32 + ['test'] * 288
#STIMULI['trial'] = range(32) + range(288)
 
for i in range(5):
    # header name for Pandas
    sequence = 'sequence' + str(i+1)
    seq = []
    
    for t in range(10): 
        random.shuffle(training)
        seq = seq + training 
        
    STIMULI[sequence] = seq



STIMULI.to_csv('stimuli_seq3.csv')
print(STIMULI)
