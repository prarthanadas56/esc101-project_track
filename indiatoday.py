import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

result = requests.get("https://www.indiatoday.in/")


soup = BeautifulSoup(result.content, "lxml")

headlines = soup.find_all("h3")

html = urlopen("https://www.indiatoday.in/")
bsObj = BeautifulSoup(html,features="lxml")

article = ''
for headline in headlines:
    print(headline.text)
    article = article + ' ' +  headline.text + '\n'

with open('indiatoday_text.txt', 'w') as file:
    file.write(article)

#for link in bsObj.findAll("a"):
    #if 'href' in link.attrs:
    	#print(link.attrs['href'])    