import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.bbc.com/news")


soup = BeautifulSoup(result.content, "lxml")

headlines = soup.find_all("h3")

article = ''
for headline in headlines:
    print(headline.text)
    article = article + ' ' +  headline.text + '\n'

with open('bbc_page.html', 'w') as file:
    file.write("<h2>"+article+"</h2></br>")