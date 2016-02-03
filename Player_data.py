import time
import re
import urllib
import urllib2
import bs4
import BeautifulSoup
import csv
import import_url
import Player_url




#for loop to get the information about the player 
#get the content in the page

count = 0
for name in urlNames:
	urlHandle_1 = urllib.urlopen(urlPlayers+name)
	html_1 = urlHandle_1.read()
	soup_1 = bs4.BeautifulSoup(html_1,"html.parser")

	trAll = soup_1.find_all("tr",{"class" : "full_table"})
 	player_data = []
	for tr in trAll:
		player_data.append(tr.get_text())     


	count+=1
	#writer the word data into the csv file
	ply_file = "player "+str(count)+".csv"
	with open(ply_file,"w") as fp:
		player_info = csv.writer(fp,delimiter = ",")
		player_info.writerows(player_data)

    


	#set the time break to prevent the malfunction of the other access

	time.sleep(1)
'''
