# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:03:10 2017

@author: ranji
"""
import unicodedata
from lxml import etree
import requests
from lxml import html
import numpy as np
import io
import re
import nltk

f=open("C:/Users/ranji/Desktop/project 660/tips.txt",'w')
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex


searchfile = open("C:/Users/ranji/Desktop/project 660/Mexican/Reviews/1.La Contenta.txt")
file_lex=loadLexicon('C:/Users/ranji/Desktop/project 660/List_lexicon_of_expressions.txt')
#stopwords=set(stopwords.words('english'))
text=searchfile.read().lower()

sentences = text.split('.')
#print(sentences)

for sent in sentences:
    #print(sent)
    sent=sent.lower().strip()
    sent=re.sub("[^a-zA-Z0-9|?|.|,|!|-|:|;|&|@|_|/|>|<|#|$|']",' ',sent)
    
    words=sent.split(' ')
    #print(words)
    
    unique=set()
    for word in words:
        #print(word)
        if word in file_lex:
            #print("heya")
            unique.add(sent)
    for i in unique:   
        f.write(str(i)+" "+"\n")
f.close()
searchfile.close()