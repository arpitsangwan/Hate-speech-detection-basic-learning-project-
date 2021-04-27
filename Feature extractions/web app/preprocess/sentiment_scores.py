
import math
import nltk
import string
from collections import defaultdict
import math
import pandas as pd
import csv
import os
import pandas as pd
import numpy as np
import nltk

# hate database
dict1=pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\dictionaries\\hatebase_dict.csv', encoding = 'ISO-8859-1')
dict11 = dict1.iloc[:,0]
dic1 = []
for row in dict11:
    row = row.strip("',")
    dic1.append(row)
    
#print(dic)
# negative words lexicon
dict2=pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\dictionaries\\negative-word.csv', encoding = 'ISO-8859-1')
dict21 = dict2.iloc[:,0]
dic2 = []
for row in dict21:
    row = row.strip("',")
    dic2.append(row)
    
# postive word lexicon
dict3=pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\dictionaries\\Postive-words.csv', encoding = 'ISO-8859-1')
dict31 = dict3.iloc[:,0]
dic3 = []
for row in dict31:
    row = row.strip("',")
    dic3.append(row)

hatedata = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\input.csv')

tweet = hatedata['clean_tweet']
hatedata=hatedata.drop(['clean_tweet','class','tweet'],axis=1)

tweet1=tweet.str.split(" ")
hate = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    count = 0
    for j in tweet1[i]:
        for g in j.split(" "):
            if g in dic1:
                count+=1
        hate[i]=count

hatenor = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    l = len(tweet1[i])
    hatenor[i] = hate[i]/l

neg = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    ct = 0
    for j in tweet1[i]:
        for g in j.split(" "):
            if g in dic2:
                ct+=1
        neg[i]=ct

negnor = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    l = len(tweet1[i])
    negnor[i] = neg[i]/l

pos = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    ct1 = 0
    for j in tweet1[i]:
        for g in j.split(" "):
            if g in dic3:
                ct1+=1
        pos[i]=ct1

posnor = np.zeros(len(tweet))
for i in range(hatedata.shape[0]):
    l = len(tweet1[i])
    posnor[i] = pos[i]/l

hatedata["hate"] = hate
hatedata["hatenor"] = hatenor
hatedata["neg"] = neg
hatedata["negnor"] = negnor
hatedata["pos"] = pos
hatedata["posnor"] = posnor

hatedata.to_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\sentiment_scores.csv',index=False)
