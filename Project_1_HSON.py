import time
import re
import urllib
from bs4 import BeautifulSoup
import csv

#web scraping

urlHandle = urllib.urlopen("http://www.basketball-reference.com/teams/?lid=front_qi_teams")
html = urlHandle.read()
soup = BeautifulSoup(html,"html.parser")

trAll = soup.find_all("tr",{"class" : "full_table"})
team_data = []
for tr in trAll:
    team_data.append(tr.get_text())     



#writer the word data into the csv file
with open("team.csv","w") as fp:
	team_info = csv.writer(fp,delimiter = ",")
	team_info.writerows(team_data)



#set the time break to prevent the malfunction of the other access

time.sleep(1)
