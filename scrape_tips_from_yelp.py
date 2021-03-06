# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 12:58:30 2017

@author: ranji
"""

from BeautifulSoup import BeautifulSoup
import re
import urllib2
from operator import itemgetter
import time
import sys
import requests
import os

def run(url):
    print(url)
    for i in range(5): # try 5 times
                  try:
                      response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                      html=response.content 
                      break 
                  except Exception as e:
                      print('failed attempt',i)
                      time.sleep(2)
                      ss=input("No internet, Enter Anything")  		
                      if not html:continue # couldnt get the page, ignore

    soup = BeautifulSoup(html) #parse the html
    page_rest=soup.findAll('div',{'class':'page-of-pages arrange_unit arrange_unit--fill'})              #To find the total page number of reviews for each restaurant to Navigate
    print(page_rest)
    pagenum=re.findall(r'Page 1 of (.*)',str(page_rest))                                                 #Pagenum gives the number of page to navigate
    print(pagenum)
    for p in range(0,int(pagenum[0])):  
        if p==0:                                                                                         #For page num=1
            print('first')
            pageLink=url 
        else:                                                                                           #For pages after
	   #print "hello"
	   pageLink=url+'?start='+str(p*20)
	
	for i in range(5): # try 5 times
	   try:
				
	       response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
	       html=response.content 
	       break 
	   except Exception as e:
	       print 'failed attempt',i
	       time.sleep(2)
	       ss=input("No internet, Enter Anything")		
	   if not html:continue # couldnt get the page, ignore

        revsoup = BeautifulSoup(html)# parse the html
        #print revsoup
                 
        review_highlights=revsoup.findAll('div',{'class': 'review-highlights'})        #Find review content with rating and date
        #print review_content
	for div in review_highlights:
	       rating_rest=revsoup.findAll('div',{'class':re.compile('i-stars i-stars--large-')}) #Scrappng rating from review content
        #for div in rating_rest:
               ra= str(rating_rest[0])
               print ra[35]
               f.write("Rating: "+ra[35])                                       #Writing Rating to the file          
               f.write('\n')
               """review_date=revsoup.findAll('span',{'class':re.compile('rating-qualifier')})
               date=str(review_date[0])
               d1=re.findall(r'class="rating-qualifier"> (.*)',str(date))
               print d1"""
               date=div.find('span')                                           #Scrapping date from review content
               if date:
                   print date.text
                   f.write("Date: "+date.text)                                 #Writing date to the file
                   f.write('\n') 
	       elem=div.find('p')                                              #Scrappng review text from review content
	       if elem:
	           print elem.text
	           try:
                    f.write(elem.text)                                         #Writting review Text to the file
                   except UnicodeEncodeError:
		    print "123"  
                   f.write('\n')
    f.close()                                                                 #Closing file 

           
if __name__=='__main__':
        path='C:\Users\ranji\Desktop\project 660\List_NY.txt'    #Reading the file from which the restaurants names are taken to search in Yelp and Scrape the reviews
        fin=open(path)
        for line in fin:                                        #For each name of restaurant in the List
                words = line.lower().strip()                     
                restraunt_name=words
                print(restraunt_name)
                restraunt_name=str(restraunt_name).replace(" ","-")
                url='https://www.yelp.com/biz/'+restraunt_name+'new-york?osq=Mexican+Food'           #Creating URL for restaurant
                f = open("C:\Users\ranji\Desktop\project 660\List_tips.txt","w")
                f.write("\n"run(url))
                f.close()