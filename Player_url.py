import time
import re
import urllib
import urllib2
import bs4
import BeautifulSoup
import csv
import import_url
#web scraping

'''
#check the dictionary works
print(import_url.urlDic)
'''
#to get the url of the teams page
urlPlayers = import_url.urlStarting+import_url.urlDic["players"]


urlHandle = urllib.urlopen(urlPlayers)
html = urlHandle.read()
soup = bs4.BeautifulSoup(html,"html.parser")

lis = soup.find_all('td',{"class" : "small_text valign_middle"})

player_url = []
for li in lis:
	url = li.find_all('a',href=True)
	for ur in url:

		href = re.findall('href="(.*)">',str(ur))
		if len(href[0]) <= 12:
			continue
		player_url.append(href[0])

#check the result
#print(player_url)


	
	

