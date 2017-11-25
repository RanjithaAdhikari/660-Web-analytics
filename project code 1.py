# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:15:37 2017

@author: ranji
the actual site for view source code : http://www.amazon.com/dp/B017HW9DEW
"""
from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep
import unicodedata
from lxml import etree
import numpy as np
import io

#scraping list of mexican rest in nyc
#f = open("C:\Users\Keval\Documents\List_hoboken.txt","w")
def ParseList():
	# Added Retrying 
    title=[]
    for i in range(5):
        try:
            s=np.arange(0,390,10)
            for n in s:
			#This script has only been tested with Amazon.com
                p_url  = 'https://www.yelp.com/search?find_desc=mexican&find_loc=New+York%2C+NY&ns=1'  #use range here of 10
			# Add some recent user agent to prevent yelp from blocking the request 
        		   headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
                page=requests.get(yelp_url,headers = headers)
    			page_response = page.text
             html_content = html.fromstring(page.content)
                 for i in range(1,10):
                     x=[]   # 
                     x=html_content.xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li['+str(i)+']/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()')
        #x1=x[0]
        #print(type(x1))
                     f.write(str(x))
        
        #title.append(x1)
                     f.close()


# In[184]:

page=requests.get('https://www.yelp.com/search?find_loc=Hoboken,+NJ&start=0')
html_content = html.fromstring(page.content)
y=html_content.xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[1]/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()')
y


# In[112]:

np.savetxt("sample.txt",npa, newline=" ")


# In[107]:




# In[105]:

str(title)


#parsing reviews from the list

def ParseReviews(asin):
	# Added Retrying 
	for i in range(5):
		try:
			#This script has only been tested with Amazon.com
			yelp_url  = 'https://www.yelp.com/biz/'+asin
			# Add some recent user agent to prevent yelp from blocking the request 
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
			page = requests.get(yelp_url,headers = headers)
          
			page_response = page.text

			parser = html.fromstring(page_response)
'''			XPATH_AGGREGATE = '//span[@id="ydeztbbffyfexswfbcdyz"]'
#span id="ydeztbbffyfexswfbcdyz" 
			XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
			XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'

			reviews = parser.xpath(XPATH_REVIEW_SECTION_1)
			if not reviews:
				reviews = parser.xpath(XPATH_REVIEW_SECTION_2)
			ratings_dict = {}
			reviews_list = []
			
			if not reviews:
				raise ValueError('unable to find reviews in page')

			#Parsing individual reviews
			for review in reviews:
				XPATH_RATING  = './/i[@data-hook="review-star-rating"]//text()'
				XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
				XPATH_REVIEW_POSTED_DATE = './/a[contains(@href,"/profile/")]/parent::span/following-sibling::span/text()'
				XPATH_REVIEW_TEXT_1 = './/div[@data-hook="review-collapsed"]//text()'
				XPATH_REVIEW_TEXT_2 = './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview'
				XPATH_REVIEW_COMMENTS = './/span[@data-hook="review-comment"]//text()'
				XPATH_AUTHOR  = './/a[contains(@href,"/profile/")]/parent::span//text()'
				XPATH_REVIEW_TEXT_3  = './/div[contains(@id,"dpReviews")]/div/text()'
				raw_review_author = review.xpath(XPATH_AUTHOR)
				raw_review_rating = review.xpath(XPATH_RATING)
				raw_review_header = review.xpath(XPATH_REVIEW_HEADER)
				raw_review_posted_date = review.xpath(XPATH_REVIEW_POSTED_DATE)
				raw_review_text1 = review.xpath(XPATH_REVIEW_TEXT_1)
				raw_review_text2 = review.xpath(XPATH_REVIEW_TEXT_2)
				raw_review_text3 = review.xpath(XPATH_REVIEW_TEXT_3)

				author = ' '.join(' '.join(raw_review_author).split()).strip('By')

				#cleaning data
				review_rating = ''.join(raw_review_rating).replace('out of 5 stars','')
				review_header = ' '.join(' '.join(raw_review_header).split())
				review_posted_date = dateparser.parse(''.join(raw_review_posted_date)).strftime('%d %b %Y')
				review_text = ' '.join(' '.join(raw_review_text1).split())

				#grabbing hidden comments if present
				if raw_review_text2:
					json_loaded_review_data = json.loads(raw_review_text2[0])
					json_loaded_review_data_text = json_loaded_review_data['rest']
					cleaned_json_loaded_review_data_text = re.sub('<.*?>','',json_loaded_review_data_text)
					full_review_text = review_text+cleaned_json_loaded_review_data_text
				else:
					full_review_text = review_text
				if not raw_review_text1:
					full_review_text = ' '.join(' '.join(raw_review_text3).split())

				raw_review_comments = review.xpath(XPATH_REVIEW_COMMENTS)
				review_comments = ''.join(raw_review_comments)
				review_comments = re.sub('[A-Za-z]','',review_comments).strip()
				review_dict = {
									'review_comment_count':review_comments,
									'review_text':full_review_text,
									'review_posted_date':review_posted_date,
									'review_header':review_header,
									'review_rating':review_rating,
									'review_author':author

								}
				reviews_list.append(review_dict)

			data = {
						'reviews':reviews_list,
					}
			return data
		except ValueError:
			print("Retrying to get the correct response")
	
	return {"error":"failed to process the page","asin":asin} '''
			
def createListandExtractReviews():
	#Add your own ASINs here 
   extracted_list = []
   f = open("C:\Users\Keval\Documents\List_hoboken.txt","w")
   for x in title:
       f.write("%s\n"%x)
       f.close()
	for l in AsinList:
		print("Downloading and processing page https://www.yelp.com/biz/"+asin)
		extracted_data.append(ParseReviews(asin))
		sleep(10)
	f=open('reviews.json','w')
	json.dump(extracted_data,f,indent=4)
	AsinList = ['el-luchador-new-york-2','maya-new-york']
	extracted_data = []
	for asin in AsinList:
		print("Downloading and processing page https://www.yelp.com/biz/"+asin)
		extracted_data.append(ParseReviews(asin))
		sleep(10)
	f=open('reviews.json','w')
	json.dump(extracted_data,f,indent=4)

if __name__ == '__main__':
	ReadAsin()