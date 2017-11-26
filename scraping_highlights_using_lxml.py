# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 17:26:54 2017

@author: ranji
"""

import unicodedata
from lxml import etree
import requests
from lxml import html
import numpy as np
import io
import numpy as np
import re, string
from nltk.tokenize.moses import MosesDetokenizer
import nltk
root = etree.Element('html')
root.tag
etree.SubElement(root,'head')
etree.SubElement(root,'body')
print(etree.tostring(root))


path='D:\\BIA\\660-Web-analytics-master\\660-Web-analytics-master\\List_NY.txt'    #Reading the file from which the restaurants names are taken to search in Yelp and Scrape the reviews
fin=open(path)
f = open("D:\\BIA\\660-Web-analytics-master\\660-Web-analytics-master\\List_NY_highlights.txt","w")
for line in fin:                                        #For each name of restaurant in the List
                words = line.lower().strip()                     
                restraunt_name=words
                #print(restraunt_name)
                #restraunt_name=str(restraunt_name).replace(" ","-")
                #url='https://www.yelp.com/biz/'+restraunt_name+'-new-york?osq=Mexican+Food'           #Creating URL for restaurant
                url='https://www.yelp.com'+restraunt_name
#page=requests.get(url)
#page=requests.get('https://www.yelp.com/biz/l-encanto-d-lola-new-york?osq=mexican+food')  
#page=requests.get('https://www.yelp.com/biz/taqueria-tlaxcalli-bronx?osq=Mexican+Food')
#                page=requests.get('https://www.yelp.com/biz/ho-brah-brooklyn?osq=Mexican+Food')
                page= requests.get(url)
#print(url)
                html_content = html.fromstring(page.content)
                for i in range(1,4):
                    x=[]
    #x=html_content.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li['+str(i)+']/div[2]/p/text()')
#                    y=html_content.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li['+str(i)+']/div[2]/p/a[1]/text()')
    #z=x+y
                    z=html_content.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li['+str(i)+']/div[2]/p/text()')
    #x=html_content1.xpath('//*[@id="super-container"]/div/div/div[1]/div[1]/div[1]/ul/li[1]/div[2]/p/text()')
    
                    z=str(z).replace('[','').replace(']','')
                    z=str(z).replace("', '\n    '","")
                    z=z.replace("'", "")
                    x = nltk.word_tokenize(z)
                    x = [''.join(c for c in s if c not in string.punctuation) for s in x]                
                    x = [s for s in x if s]
                    x1= list(filter(('n').__ne__, x))    
                    detokenizer = MosesDetokenizer()
                    list1=detokenizer.detokenize(x1, return_str=True)
                    list1.strip()
                    list1 = list1[1:-1]
                    print(list1)
                    f.write("%s\n"%list1)
f.close()   
