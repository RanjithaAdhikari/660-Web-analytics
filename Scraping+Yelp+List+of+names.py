import unicodedata
from lxml import etree
import requests
from lxml import html
import numpy as np
import io
import numpy as np

root = etree.Element('html')
root.tag
etree.SubElement(root,'head')
etree.SubElement(root,'body')
print(etree.tostring(root))

s=np.arange(0,390,10)

f = open("C:\\Users\\ranji\\Desktop\\project 660\\List_NY.txt","w")

title=[]
for j in s:    
    page=requests.get('https://www.yelp.com/search?find_desc=Mexican+Food&find_loc=New+York,+NY&start='+str(j))
    html_content = html.fromstring(page.content)
    for i in range(3,11):
        x=[]
        x=html_content.xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li['+str(i)+']/div/div[1]/div[1]/div/div[2]/h3/span/a/@href')
        y=str(x).replace(',','Mexican').replace("'","").replace('[','').replace(']','')
        f.write("%s\n"%y)
f.close()
'''for i in range(3,13):
    pages=requests.get('https://www.yelp.com/search?find_desc=mexican+food&find_loc=New+York%2C+NY&ns=1')
    html_contents=html.fromstring(pages.content)
    a=html_contents.xpath('//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li['+str(i)+']/div/div[1]/div[1]/div/div[2]/h3/span/a/@href')
    print('https://www.yelp.com%s'%a)'''
    
#//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[3]/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()
#//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[4]/div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()
#//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[12]/div/div[1]/div[1]/div/div[2]/h3/span/a/span
#//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[3]/div/div[1]/div[1]/div/div[2]/h3/span/a/span
#//*[@id="super-container"]/div/div[2]/div[1]/div/div[4]/ul[2]/li[2]/div/div[1]/div[1]/div/div[2]/h3/span/a/span
