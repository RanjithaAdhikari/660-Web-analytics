# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 18:14:27 2017

@author: ranji
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time


def run(url):	
    for p in range(0,300,10): # for each page 
        print ('page',p)
        html=None
       
        if p==0: pageLink=url # url for page 1
        
        else: pageLink=url+'&start='+str(p) # make the page url
		
        for i in range(5):
            try:
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2) 
				
		
        if not html:continue 
    
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml',from_encoding="utf-8")
        links = soup.find_all("h3",{"class":"search-result-title"})  # it finds the urls of the indian/chinese restro
        
        for link in links[1:]:
            res_name = ''.join(map(lambda x: x.strip(), link.strings))
#            print(res_name)
            
            res_url = 'https://www.yelp.com/' + link.find('a').get('href')
#            print(res_url)
            file_path_name_review = 'C:/Users/ranji/Desktop/project 660/Mexican/Reviews/'+str(res_name)+'.txt'
            REVIEW_file = open(file_path_name_review,'a')
            print(res_name)
            for review_page in range(0,300,20):
                if not re.search('adredir',res_url): # the if condition is used to filter all ads
                    replaced_url = 'start='+str(review_page)
                    review_url = res_url.replace('osq=Restaurants+-+Indian',replaced_url)
                    counter = 0
                    for i in range(5):
                        try:
                            response_review=requests.get(review_url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                            html=response_review.content 
                            break 
                        except Exception as e:
                            print ('failed attempt to fetch review for ',res_name)
                            time.sleep(2) 
				
		
                    if not html:continue 
                    print(review_url)
                    review_html = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml',from_encoding="utf-8") #html file for review
#                    print(review_html) 


########################## wrtiting the source code to txt files ##########################################
                    file_path_name = 'C:/Users/ranji/Desktop/project 660/Mexican/Html/'+str(res_name)+'_'+str(review_page)+'(Source_Code).txt'
                    HTML_file = open(file_path_name,'w')
                    HTML_file.write(review_html.text)
                    HTML_file.close()

########################## wrtiting the source code to txt files ##########################################
    
                    reviews = review_html.findAll('div', {'class':'review-content'})
                    for review in reviews: 
                        review_content = review.find('p',{'lang':'en'}) 
                        data = review_content.text
                        REVIEW_file.write(data)
                        REVIEW_file.write('\n')
                        counter = counter + 1
                    print(counter)
                   
            REVIEW_file.close()
#           
#                        
    print('success')       
                    
url = "https://www.yelp.com/search?find_desc=Restaurants+-+mexican&find_loc=New+York,+NY"
run(url)