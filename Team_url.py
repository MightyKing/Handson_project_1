import time
import re
import urllib
from bs4 import BeautifulSoup
import csv
import import_url
#web scraping

'''
#check the dictionary works
print(import_url.urlDic)
'''
#to get the url of the teams page
urlTeam = import_url.urlStarting+import_url.urlDic["teams"]

urlHandle = urllib.urlopen(urlTeam)
html = urlHandle.read()
soup = BeautifulSoup(html,"html.parser")

trAll = soup.find_all("td",{"align" : "left"})
team_url = []
for td in trAll:
	a = td.find_all('a')
	if a == []:
		continue
	href = re.findall('href="/(.*)">',str(a))
	team_url.append(href)     

#print(team_url) 
#the team_url dataset is the dataset for the urls of the each team







#set the time break to prevent the malfunction of the other access

time.sleep(1)
