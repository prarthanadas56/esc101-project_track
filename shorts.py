import requests
from bs4 import BeautifulSoup
import json


def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    article = ''
    for headline in headlines:
        print("    " + headline.text)
        article = article + ' ' +  headline.text + '\n'
        
    with open('shorts_text.txt', 'w') as file:
    	file.write(article)




    with open('shorts_page.html', 'w') as file:
    	file.write("<h1>"+"INSHORTS NEWS-HEADLINES"+"</h1></br>") 
    	file.write("<h2>"+article+'\n'+"</h2></br>")
         
url = 'https://inshorts.com/en/read'
response = requests.get(url)
print_headlines(response.text)

   