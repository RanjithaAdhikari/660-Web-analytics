# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:15:58 2017

@author: ranji
"""

import os
import time
from bs4 import BeautifulSoup

cuisine = input("Enter the cuisine: ")
path = "C:/Users/ranji/Desktop/project 660/"+cuisine+"/"

for filename in os.listdir(path):
    restaurant_name = filename
    restaurant_name = restaurant_name.split("_review",1)[0]
    print(restaurant_name)

    soup = None
    for i in range(5):  # try 5 times
        try:
            soup = BeautifulSoup(open(path+filename, encoding="utf-8"),"html.parser")
            break  # we got the file, break the loop
        except Exception as e:  # browser.open() threw an exception, the attempt to get the response failed
            print('failed attempt', i)
            time.sleep(2)  # wait 2 secs

    if not soup: continue  # couldnt get the page, ignore

    reviews = soup.findAll('div', {'class': 'review-content'})  # get all the review divs
    for review in reviews:
        text = review.find('p',{'lang': 'en'})
        if text:
            with open(restaurant_name+".txt",'a+') as f:
                f.write(text.text + '\n')