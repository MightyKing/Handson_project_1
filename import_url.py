import re
import urllib2
import BeautifulSoup

#identify the starting URL to crawl
urlStarting = "http://www.basketball-reference.com/"

#using the regex and the beautifulsoup to crawl the data from the page
request = urllib2.Request(urlStarting)
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
lis = soup.findAll('div',{"id" : "quick_index"})

#store the url data into the list called urlNames
urlNames = re.findall('href="/(.*)">.*</a>',str(lis))

'''
#check if it works
for i in range(0,len(urlNames)-1):
	print(urlNames[i])
'''


#establish the dictionary for the url names
urlDic = {}
for i in range(0,len(urlNames)):
	name = re.findall("(.*)/\?lid=",urlNames[i])
	urlDic[name[0]] = urlNames[i]

'''
#check the dictionary
print(urlDic)	
'''









		

