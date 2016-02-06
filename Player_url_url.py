import time
import re
import urllib
import urllib2
import bs4
import BeautifulSoup
import csv
import import_url
import Player_url
#web scraping

'''
#check the dictionary works
print(import_url.urlDic)
'''
#to get the url of the teams page
count = 1
player_dic = {}
for url_lower in Player_url.player_url:
	

	urlPlayers = import_url.urlStarting+url_lower
	

	urlHandle = urllib.urlopen(urlPlayers)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	lis = soup.find_all('tr',{"class" : ""})

	player_url = []
	for li in lis:
		url = li.find_all('a',href=True)
		
		for ur in url:
			
			href = re.findall('href="/(players/.*)">',str(ur))
			if href == []:
				continue
			if len(href[0]) <= 12:
				continue
			
			player_url.append(href[0])
	player_url_2 = []
	
	for url in player_url:
		url_2 = import_url.urlStarting+url
		player_url_2.append(url_2)
	
	player_dic[str(count)] = player_url_2
	count+=1


	time.sleep(1)
#check the result

#print(player_dic)

	
	

