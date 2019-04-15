import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.ndtv.com/")


soup = BeautifulSoup(result.content, "lxml")

headlines = soup.find_all("h3")

article = ''
for headline in headlines:
    print(headline.text)
    article = article + ' ' +  headline.text + '\n'
with open('ndtv_text.txt', 'w') as file:
    file.write(article)
