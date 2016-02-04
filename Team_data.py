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


out = open('team.csv','w')
team_info = csv.writer(out,delimiter = ",")

for url in Team_url.team_url[0:1]:
	team_title = []
	teamUrl = import_url.urlStarting+url[0]
	print(teamUrl)
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	trAll = soup.find_all("tr",{"class" : ""})
	
	
	for tr in trAll:
		th = tr.find_all('th')
		for t in th:
			team_title.append(t.get_text().encode('utf8'))
	#set the time break to prevent the malfunction of the other access
	
	team_info.writerow(team_title)


	time.sleep(1)


for url in Team_url.team_url:
	
	teamUrl = import_url.urlStarting+url[0]
	print(teamUrl)
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	trAll = soup.find_all("tr",{"class" : ""})
	
	
	for tr in trAll:

		team_data = []
		td = tr.find_all('td')
		
		if td == []:
			continue
		
		for t in td:
			team_data.append(t.get_text().encode('utf8'))
		
		team_info.writerow(team_data)
	
	#set the time break to prevent the malfunction of the other access
	
	


	time.sleep(1)

		
#writer the word data into the csv file


out.close()	







