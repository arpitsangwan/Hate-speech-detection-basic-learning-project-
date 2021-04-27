

import pandas as pd
import numpy as np
import string
import csv


#read in each of the feature csv files
class_labels = pd.read_csv("C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\labels.csv",encoding='utf-8')
weighted_tfidf_score = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\\\tfidf_scores.csv',encoding='utf-8')
sentiment_scores = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\\\sentiment_scores.csv',encoding='utf-8')
word_bigrams = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\word_bigram_features.csv',encoding='utf-8')
tfidf_sparse_matrix = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Feature extractions\\web app\\preprocess\\tfidf_features.csv',encoding='utf-8')

#merge all feature data sets based on 'index' column sentiment_scores, dependency_features, char_bigrams, word_bigrams
df_list=[class_labels, weighted_tfidf_score,sentiment_scores,word_bigrams, tfidf_sparse_matrix]
master = df_list[0]
for df in df_list[1:]:
    master = master.merge(df, on='index')

master.columns.values
#ignore first two columns (index and tweet)

X=master.iloc[:,3:] #all features


