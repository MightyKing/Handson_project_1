from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv
import timeit
import time
import re
import Player_url_url

def outputcsv(player_name,table_name):
	out.write("Name"+","+"Table"+",")
	
	for j in header.find_all("th"):
		out.write(j.get_text()+",")
	out.write("\n")

	
	for i in table:
		out.write(player_name+","+table_name+",")
		
		for j in i.find_all("td"):
			out.write(j.get_text().encode('utf8')+",")
		out.write("\n")
	out.write("\n")

out = open('out_player_data.csv','w')
start = timeit.default_timer()


for count in range(1,26):
	

	for url in Player_url_url.player_dic[str(count)]:
		webpage = urlopen(url).read()
		soup = BeautifulSoup(webpage, "html.parser")
		player_name = soup.find_all("h1")[0].get_text().encode('utf8')
		

		
		


		table = soup.find("table",{"id":"per_minute"}).find_all("tr",{"class":"full_table"})
		header = soup.find("table",{"id":"per_minute"}).find("thead")
		outputcsv(player_name,"per_minute")


		
		


out.close()

stop = timeit.default_timer()
print stop - start

time.sleep(1)

