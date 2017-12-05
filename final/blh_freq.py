# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:01:39 2017

@author: ranji
"""
import nltk
from nltk.util import ngrams 
import re
from nltk.tokenize import sent_tokenize
from nltk import load
from textblob import TextBlob, Word
import sys
import random
from collections import Counter
import csv

f=open('C:/Users/ranji/Desktop/project 660/final/tips.txt')
fn=open('C:/Users/ranji/Desktop/project 660/final/nouns.txt','w')
text=f.read().strip()
f.close()
blob = TextBlob(text)

nouns = list()
for word, tag in blob.tags:
    if tag == 'NN':
        nouns.append(word.lemmatize())
nouns=[x for x in nouns if x != 'i']
fn.write(str(nouns))
#print(nouns)
freqNouns = Counter(nouns)

#print(freqNouns)
#fc.write(str(freqNouns))
#print(type(freqNouns))
'''with fc as f:
    for k,v in freqNouns:
        fc.write( "{} {}\n".format(k,v) )'''
with open('C:/Users/ranji/Desktop/project 660/final/counter.csv','w') as csvfile:
    #print(nouns)
    writer=csv.writer(csvfile,dialect='excel')
    for noun in nouns:
        if noun:
            writer.writerow([noun])