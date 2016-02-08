from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import re
import import_url
import Player_url
import time




out6 = open('out_p_bi.csv','w')


out6.write("Player,From,To,Pos,Ht,Wt,Birth_Date,College")           
out6.write("\n")

#need to change following url name#
for ur in Player_url.player_url:
    url = import_url.urlStarting + ur
    print(url)
    webpage = urlopen(url).read()
    soup = BeautifulSoup(webpage,"html.parser")
    table=soup.findAll("tr",{"class" : ""})

    for ta in table[1:]:
        print(ta)
        player=re.findall('html">(.*?)</a>',str(ta))
        value=ta.findAll("td")
        print(value)
        From =re.findall('">(.*?)</',str(value[1]))
        To =re.findall('">(.*?)</',str(value[2]))
        Pos =re.findall('">(.*?)</',str(value[3]))
        Ht =re.findall('">(.*?)</',str(value[4]))
        Wt =re.findall('">(.*?)</',str(value[5]))
        if re.findall('">([^<].*?)</',str(value[6])) != []:
            Birth_date =re.findall('">([^<].*?),',str(value[6]))
            Birth_year =re.findall(', (.*?)</',str(value[6]))
            Birth = Birth_date[0]+"/"+Birth_year[0]
        else:
            Birth = ""
        if re.findall('">([^<].*?)</',str(value[7])) != []:
            if re.findall("(,)",re.findall('">([^<].*?)</',str(value[7]))[0]) != []:
                College_1 =re.findall('">([^<].*?),',str(value[7]))
                College_2 =re.findall(',(.*?)</',str(value[7]))
                College = College_1[0]+"/"+College_2[0]
            else:
                College = re.findall('">([^<].*?)</',str(value[7]))[0]
        else:
            College = ""
        out6.write(str(player[0])+",")
        out6.write(str(From[0])+",")
        out6.write(str(To[0])+",")
        out6.write(str(Pos[0])+",")
        out6.write("'"+str(Ht[0])+"'"+",")
        out6.write(str(Wt[0])+",")
        print(str(Birth_date[0]))
        out6.write(str(Birth)+",")
        out6.write(str(College)+",")
        out6.write("\n")

    time.sleep(1)




out6.close()
print 'done'
