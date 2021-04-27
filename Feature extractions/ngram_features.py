from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import nltk
import string
import re
import pandas as pd
import numpy as np
from nltk import word_tokenize

data = pd.read_csv('C:\\Users\\arpit\\OneDrive\\Desktop\\AI\\Extracted datasets\\cleaned_tweets.csv',encoding='utf-8')

stemmer = SnowballStemmer("english")
data['stemmed'] = data.clean_tweet.map(lambda x: ' '.join([stemmer.stem(y) for y in x.split(' ')]))

#WORD LEVEL N-GRAMS (keep numbers as they represent unicode for emojis)
cv = CountVectorizer(stop_words='english', min_df=.002, max_df=.8, ngram_range=(2,2))
cv.fit(data.stemmed)
cv_mat = cv.transform(data.stemmed)

bigrams = pd.DataFrame(cv_mat.todense(), index=data['index'], columns=cv.get_feature_names())
bigrams = bigrams.add_prefix('word_bigrams:')
bigrams.to_csv('word_bigram_features.csv')



###########################################################################################################
#TFIDF VALUES
cv = CountVectorizer(stop_words='english', min_df=.002, max_df=.8, ngram_range=(1,1))
cv.fit(data.stemmed)
cv_mat = cv.transform(data.stemmed)

transformer = TfidfTransformer()
transformed_weights = transformer.fit_transform(cv_mat)

weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term': cv.get_feature_names(), 'weight': weights})
weights_df.sort_values(by='weight', ascending=False).head(80)
transformed_weights.toarray()

tf_idf =pd.DataFrame(transformed_weights.todense(), index=data['index'], columns=cv.get_feature_names())

tf_idf = tf_idf.add_prefix('tfidf:')

tf_idf.to_csv('tfidf_features.csv')
