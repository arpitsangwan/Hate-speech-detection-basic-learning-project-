 
import pandas as pd
import numpy as np
import string
import csv
   
exec(open('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\sentiment_scores.py').read())
exec(open('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\tf-idf.py').read())





#read in each of the feature csv files
class_labels = pd.read_csv("C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\labels.csv",encoding='utf-8')
sentiment_scores = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\sentiment_scores.csv',encoding='utf-8')
tfidf_scores=pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\tfidf_scores.csv',encoding='utf-8')

#merge all feature data sets based on 'index' column sentiment_scores, dependency_features, char_bigrams, word_bigrams
df_list=[class_labels,sentiment_scores,tfidf_scores]
master= df_list[0]
for df in df_list[1:]:
    master= master.merge(df, on='index')

master.columns.values
#ignore first two columns (index and tweet)
ye=master.iloc[:,3:] #all features
