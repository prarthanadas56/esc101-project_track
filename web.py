import argparse
import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pygraphviz import *
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


result = requests.get("https://www.indiatoday.in/")


soup = BeautifulSoup(result.content, "lxml")

headlines = soup.find_all("h3")
parser = argparse.ArgumentParser(description='News Crawler')
parser.add_argument('url', metavar='url', type=str,
                    help='The url of the page where to start.')
parser.add_argument('-o', metavar='output_filename', dest="output_filename", type=str, default="output",
                    help='The output filename.')

arguments = parser.parse_args()
graph = AGraph(directed=True, rank="same")


html = urlopen("https://www.indiatoday.in/")
bsObj = BeautifulSoup(html,features="lxml")




def extract_domain(url):
    try:
        domain = next(re.finditer(":\/\/[^/]+", url)).group()[3:]
        return domain
    except Exception as e:
        return None


def extract_title(response):
    try:
        title = Selector(text=response.body).xpath('//title/text()').extract()[0]
        title = title.strip()
        return title
    except Exception as e:
        return ""


def make_node_label(response):
    return (extract_title(response) + "\n" + response.request.url).strip()


class SimpleSpider(CrawlSpider):
    name = 'simplespider'

    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True,)]
    # custom_settings = {'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter'}

    def parse_start_url(self, response):
        graph.add_node(response.request.url, label=make_node_label(response))
        request = super(SimpleSpider, self).parse_start_url(response)
        return request

    def _requests_to_follow(self, response):
        for r in super(SimpleSpider, self)._requests_to_follow(response):
            r.meta["parent_url"] = response.request.url
            yield r

    def parse_item(self, response):
        current_url = response.request.url

        if extract_domain(current_url) != self.allowed_domains[0]:
            return
        graph.add_node(current_url, label=make_node_label(response))

        parent_url = response.meta["parent_url"]
        graph.add_edge(parent_url, current_url)


def main():
    article = ''
    for headline in headlines:
        print(headline.text)
        article = article + ' ' +  headline.text + '\n'

    with open('indiatoday_text.txt', 'w') as file:
        file.write(article)


    start_url = arguments.url
    domain = extract_domain(start_url)
    if domain is None:
        print ("Error: Cannot find domain name in the url.")
        exit(1)

    print ("Starting url: %s" % start_url)
    print ("Domain: %s" % domain)

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(SimpleSpider, start_urls=[start_url], allowed_domains=[domain])
    process.start()  # the script will block here until the crawling is finished

    graph.graph_attr["rankdir"] = "LR"
    graph.layout("dot")
    graph.draw(arguments.output_filename, format="svg")



if __name__ == '__main__':
    main()





