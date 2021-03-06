from bs4 import BeautifulSoup
import requests
import pandas as pd

starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(starturl)
print(page)
soup=BeautifulSoup(page.text,'html.parser')
starTable=soup.find('table')
templist=[]
tablerows=starTable.find_all('tr')
for tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    templist.append(row)
starnames=[]
distance=[]
mass=[]
raduis=[]
lum=[]
for i in range (1,len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    raduis.append(templist[i][6])
    lum.append(templist[i][7])
df2=pd.DataFrame(list(zip(starnames,distance,mass,raduis,lum)),columns=["starnames","distance","mass","raduis","lum"])
print(df2)
df2.to_csv('bright stars.csv')



