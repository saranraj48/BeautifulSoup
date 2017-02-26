"""Ieee Website link to retrive the Beautiful Soup"""
from bs4 import BeautifulSoup
import urllib2 

#url link access
url="http://ieee.org"

#request the url 
req=urllib2.urlopen(url)
page=req.read()

#scarping the web page
scraping=BeautifulSoup(page)
alllink=scraping.findAll("a",text=True)
print alllink
#print alllink[0]

with open("bseindex3.out","w") as f:
    for i in alllink:
        #print i
        href=i.get("href")
        name=i.string
        name=name.strip()
        #print href
        #print name
        if(href!="#"):   
            f.write("{0}, {1} \n".format(name,href))


