 # -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:48:14 2023

@author: linus
""" 

from iterate_over_DB import iterate_over_database
if __name__ == '__main__':
    iterate_over_database(path="Results/",exelname="biomodels")
'''
import os
models = []
for root, dirs, files in os.walk('D:/Github/dorganalysis/code/Results'):
    for file in files:
        if file.endswith('.xml'):
            print(file)
            models.append(file)
            
import pandas as pd
df = pd.read_csv('D:/Github/dorganalysis/code/biomodels FULL.csv')

IDs = df['ID'].to_list()
index = []

for i in range(len(df)):W
    if IDs[i] in models:
        index.append(i)
    
df_cellcycle = df.loc[index]
df_cellcycle.to_csv('biomodels Cell cycles from FULL (234).csv')
'''
