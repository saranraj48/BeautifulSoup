"""Beautiful Soup"""
from bs4 import BeautifulSoup
from urllib2 import urlopen
print "\n******espncricinfo.com******"

# to find the score use www.espncricinfo.com
#url = raw_input("Enter the URL to fetch:")
url = "http:// www.espncricinfo.com"

# hit the url and store the response
response = urlopen(url).read()

# pass the response to soup
Soup=BeautifulSoup(response , "html.parser")

# parse using soup to find the appropriate result
Score = Soup.find("ul",attrs = {"class":"scoreline-list"})

india_vs_srilanka = Score.findChild()

for element in india_vs_srilana.findAll('span'):
    print element.text.strip()

