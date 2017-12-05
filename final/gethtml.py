# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:50:40 2017

@author: ranji
"""

from bs4 import BeautifulSoup
import time
import re
from urllib.request import urlretrieve
import requests

def run(url):
    pagenumber = 0
    print (url)
    for p in range(0,100,20):
        pagenumber = pagenumber + 1
        html=None
        pageLink=url+'?start='+str(p) # make the page url
        for i in range(5): # try 5 times
            try:
                reviewName ='rosies-new-york_review_pg'+ str(pagenumber) + '.html'
                urlretrieve(pageLink,reviewName)
                print(pageLink)
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
        if not html:continue # couldnt get the page, ignore


if __name__ == '__main__':
    url='https://www.yelp.com/biz/rosies-new-york-2?osq=Mexican+Food'
    run(url)
