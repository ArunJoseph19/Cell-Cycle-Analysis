# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:15:18 2024

@author: A ARUN JOSEPHRAJ
"""
import json
import os
import pandas as pd

files = os.listdir('Parameters_ALL/')
parameters = []

temp = 0
for i in files:
    with open('Parameters_ALL/'+str(i)) as f:
        data = json.load(f)
        print(len(data.keys()))
        if len(data.keys()) == 1:
            temp+=1

P = []
for i in range(len(list(data.keys()))+1):
    P.append([])

params = list(data.keys())

for i in files:
    with open('Parameters_ALL/'+str(i)) as f:
        data = json.load(f)
        if len(data.keys()) != 1:
            P[0].append(i)
            for j in range(1,14):
                P[j].append(data[params[j-1]])
        else:
            print(i)


df = pd.DataFrame(P)
df = df.T
df.columns = ['Model name'] + params
# Write the DataFrame to a CSV file
df.to_csv('Parameters_all.csv', index=False)


df = pd.read_csv('Biomodels cell cycles - Parameters.csv')
df2 = pd.read_csv('Biomodels cell cycles - FULL 16th April.csv')

time = []
for i in df['Model name'].to_list():
    for j in range(len(df2)):
        if i == df2['ID'][j]:
            time.append(df2['time_complete'][j])

for i in range(len(time)):
    if time[i][0:2] == '0,':
        time[i] = float(time[i].replace(',','.'))
            
df = pd.DataFrame(time)
df.to_csv('Time.csv', index=False)