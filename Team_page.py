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
