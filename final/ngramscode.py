# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:18:57 2017

@author: ranji
"""

"""

The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging

The run function includes all 2grams of the form: <ADVERB> <ADJECTIVE>

POS tags list: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
"""

import nltk
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load

# return all the 'adv adj' twograms
def getAdvAdjTwograms(terms,adj,adv):
    result=[]
    twograms = ngrams(terms,2) #compute 2-grams    
   	 #for each 2gram
    for tg in twograms:  
        if tg[0] in adv and tg[1] in adj: # if the 2gram is a an adverb followed by an adjective
            result.append(tg)

    return result

def getAdjOnegrams(terms,adj):
    resultadj=[]
    onegrams = ngrams(terms,1) #compute 2-grams    
   	 #for each 2gram
    for og in onegrams:  
        if og[0] in adj: # if the 2gram is a an adverb followed by an adjective
            resultadj.append(og[0])

    return resultadj

'''def getVerAdvAdjThreegrams(terms,ver,adj,adv):
    result=[]
    threegrams = ngrams(terms,3) #compute 2-grams    
   	 #for each 2gram
    for tg in threegrams:  
        if tg[0] in ver and tg[1] in adv and tg[2] in adj: # if the 2gram is a an adverb followed by an adjective
            result.append(tg)

    return result
'''

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms


def run1(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    adjAfterAdv=[]

    # for each sentence
    for sentence in sentences:

        #sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        #sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces, one or more spaces ' +'

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence)   

        POStags=['JJ','RB'] # POS tags of interest 		
        POSterms=getPOSterms(terms,POStags,tagger)

        adjectives=POSterms['JJ']
        adverbs=POSterms['RB']

        #get the results for this sentence 
        adjAfterAdv+=getAdvAdjTwograms(terms, adjectives, adverbs)
        #adjAfterAdv+=getAdjOnegrams(terms, adjectives)
        newadjAfterAdv=set(adjAfterAdv)
		
    return newadjAfterAdv

def run2(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    adjAfterAdv=[]

    # for each sentence
    for sentence in sentences:

        #sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        #sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces, one or more spaces ' +'

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence)   

        POStags=['JJ','RB'] # POS tags of interest 		
        POSterms=getPOSterms(terms,POStags,tagger)

        adjectives=POSterms['JJ']
        adverbs=POSterms['RB']

        #get the results for this sentence 
        #adjAfterAdv+=getAdvAdjTwograms(terms, adjectives, adverbs)
        adjAfterAdv+=getAdjOnegrams(terms, adjectives)
        newadjAfterAdv=set(adjAfterAdv)
		
    return newadjAfterAdv

'''
def run3(fpath):

    #make a new tagger
    _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
    tagger = load(_POS_TAGGER)

    #read the input
    f=open(fpath)
    text=f.read().strip()
    f.close()

    #split sentences
    sentences=sent_tokenize(text)
    print ('NUMBER OF SENTENCES: ',len(sentences))

    adjAfterAdv=[]

    # for each sentence
    for sentence in sentences:

        #sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        #sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces, one or more spaces ' +'

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence)   

        POStags=['V','JJ','RB'] # POS tags of interest 		
        POSterms=getPOSterms(terms,POStags,tagger)

        verbs=POSterms['V']
        adjectives=POSterms['JJ']
        adverbs=POSterms['RB']

        #get the results for this sentence 
        #adjAfterAdv+=getAdvAdjTwograms(terms, verbs,adjectives, adverbs)
        adjAfterAdv+=getAdjOnegrams(terms, adjectives)
        newadjAfterAdv=set(adjAfterAdv)
		
    return newadjAfterAdv
'''

if __name__=='__main__':
    run1=run1('List_NY_highlights.txt')
    run2=run2('List_NY_highlights.txt')
    #print (run1('List_NY_highlights.txt'))
    #print (run2('List_NY_highlights.txt'))
    f = open("C:\\Users\\ranji\\Desktop\\project 660\\List_lexicon_of_expressions.txt","w")
    for elem in run1:
        for elemlist in elem:
            f.write(str(elemlist)+" ")
        f.write("\n")
    for elem in run2:
        f.write("\n"+str(elem))
    f.close()
    #print (run3('List_NY_highlights.txt'))



