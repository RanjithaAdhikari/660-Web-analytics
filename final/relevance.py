# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:53:19 2017

@author: ranji
"""

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import random
from sklearn.preprocessing import StandardScaler
from pylab import rcParams #set figure size
import csv
from sklearn.decomposition import PCA
import pandas as pd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
f=open("relevant.txt",'w')
# train word2vec on your file
model0 = Word2Vec(LineSentence("C:/Users/ranji/Desktop/project 660/final/counter.csv"), size=10, window=2, min_count=1, workers=4)
#model0['restaurant']
list1=model0.most_similar('food', topn=10)
print((list1[0]))
with open("C:/Users/ranji/Desktop/project 660/final/relevant.csv","w") as result:
    wr = csv.writer(result,dialect="excel")
    for each in list1:
        if each:
            wr.writerow(each)