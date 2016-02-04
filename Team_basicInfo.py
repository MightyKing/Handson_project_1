import time
import re
import urllib
import urllib2
import bs4
import BeautifulSoup
import csv
import import_url
import Team_url


#loop for the each team's page to get the data

out = open('team_basicInfo.csv','w')
team_info = csv.writer(out,delimiter = ",")



for url in Team_url.team_url[0:1]:
	teamUrl = import_url.urlStarting+url[0]
	
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	divAll = soup.find_all("div",{"class" : "mobile_text"})
	for div in divAll:
		text = div.find_all('span')
		team_basic = []
		for tx in text:
			team_basic.append(tx.get_text().encode('utf8'))
		
        team_info.writerow(team_basic)
		
	
	#set the time break to prevent the malfunction of the other access

	time.sleep(1)


for url in Team_url.team_url:
	teamUrl = import_url.urlStarting+url[0]
	
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	divAll = soup.find_all("div",{"class" : "mobile_text"})
	for div in divAll:
		
		
		tx = re.findall('</span> (.*?)\n',str(div))
		
        team_info.writerow(tx)
		
	
	#set the time break to prevent the malfunction of the other access

	time.sleep(1)


#The wrong part of the basic info
'''
team_basic = []
for url in Team_url.team_url[0:1]:
	teamUrl = import_url.urlStarting+url[0]
	
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	divAll = soup.find_all("div",{"class" : "mobile_text"})
	for div in divAll:
		
		data = re.findall('/span>(.*){0,60}<[^/]',str(div))
		print(data)

		team_title.append(p.get_text().encode('utf8'))
	
	#set the time break to prevent the malfunction of the other access

	time.sleep(1)
'''


#writer the word data into the csv file

	
out.close()







