from urllib2 import urlopen
from bs4 import BeautifulSoup
import csv
import timeit

def outputcsv():
	for j in header.find_all("th"):
		out.write(j.get_text()+",")
	out.write("\n")

	for i in table:
		for j in i.find_all("td"):
			out.write(j.get_text().encode('utf8')+",")
		out.write("\n")
	out.write("\n")

start = timeit.default_timer()

webpage = urlopen('http://www.basketball-reference.com/players/a/abdulka01.html').read()
soup = BeautifulSoup(webpage, "html.parser")
out = open('out.csv','w')

table = soup.find("table",{"id":"totals"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"totals"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"per_game"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"per_game"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"per_minute"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"per_minute"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"per_poss"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"per_poss"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"advanced"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"advanced"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"playoffs_totals"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"playoffs_totals"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"playoffs_per_game"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"playoffs_per_game"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"playoffs_per_minute"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"playoffs_per_minute"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"playoffs_per_poss"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"playoffs_per_poss"}).find("thead")
outputcsv();

table = soup.find("table",{"id":"playoffs_advanced"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"playoffs_advanced"}).find("thead")
outputcsv();

print(soup.find("table",{"id":"all_star"}))
table = soup.find("table",{"id":"all_star"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"all_star"}).find("thead")
outputcsv();

out.close()

stop = timeit.default_timer()
print stop - start

