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
team_data = []
for url in Team_url.team_url:
	teamUrl = import_url.urlStarting+url[0]
	print(teamUrl)
	urlHandle = urllib.urlopen(teamUrl)
	html = urlHandle.read()
	soup = bs4.BeautifulSoup(html,"html.parser")

	trAll = soup.find_all("tr",{"class" : ""})
	
	for tr in trAll:
		team_data.append(tr.get_text().encode('utf8'))

	#set the time break to prevent the malfunction of the other access

	time.sleep(1)


#writer the word data into the csv file

with open("team.csv","w") as fp:
	team_info = csv.writer(fp,delimiter = ",")
	team_info.writerows(team_data)







