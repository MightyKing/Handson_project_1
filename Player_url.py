import time
import re
import urllib
import urllib2
import bs4
import BeautifulSoup
import csv
import import_url
import timeit
#web scraping

'''
#check the dictionary works
print(import_url.urlDic)
'''
#to get the url of the teams page

start = timeit.default_timer()
urlPlayers = import_url.urlStarting+import_url.urlDic["players"]


urlHandle = urllib.urlopen(urlPlayers)
html = urlHandle.read()
soup = bs4.BeautifulSoup(html,"html.parser")

lis = soup.find_all('td',{"class" : "align_center bold_text valign_bottom xx_large_text"})

player_url = []
for li in lis:
	url = li.find_all('a',href=True)
	for ur in url:

		href = re.findall('href="/(.*)">',str(ur))
		player_url.append(href[0])

#check the result
#print(player_url)
stop = timeit.default_timer()

print stop - start

	
	

