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

out = open('salaries.csv','w')
start = timeit.default_timer()


for count in range(1,26):
	

	for url in Player_url_url.player_dic[str(count)]:
		print(url)
		webpage = urlopen(url).read()
		soup = BeautifulSoup(webpage, "html.parser")
		player_name = soup.find_all("h1")[0].get_text().encode('utf8')
		

		
		
		if soup.find("table",{"id" : "salaries"}) == None:
			continue
		table = soup.find("table",{"id" : "salaries"}).find_all("tbody")[0].find_all("tr",{"class" : ""})
		header = soup.find("table",{"id" : "salaries"}).find("thead")

		out.write("Name"+","+"Table"+",")
		for j in header.find_all("th"):
			out.write(j.get_text()+",")
		out.write("\n")
		table_name = "salaries"
		for i in table:
			out.write(player_name+","+table_name+",")
			for j in i.find_all("td"):
				if re.findall("(,)",j.get_text().encode('utf8')) != []:
					x = re.findall("(.*),",j.get_text().encode('utf8'))[0]
					y = re.findall(",(.*)",j.get_text().encode('utf8'))[0]
					text = x+y
				else:
					text = j.get_text().encode('utf8')
				out.write(text+",")
			out.write("\n")
		out.write("\n")
		


out.close()

stop = timeit.default_timer()
print stop - start

time.sleep(1)

