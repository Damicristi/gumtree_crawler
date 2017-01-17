import requests
from bs4 import BeautifulSoup

gumtree = 'http://www.gumtree.com.au/s-appliances/doncaster-melbourne/page-2/c20088l3001540'

def trade_spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a',{'class':'ad-listing__title-link'}):
        href ='http://www.gumtree.com.au/'+link.get('href')


        print (href)

        get_name(href)

        get_single_item_data(href)

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('dd',{'clsaa','ad-details__ad-attribute-value'}):
        print(item_name.string)

def get_name(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('h1',{'itemprop':'name'}):
        title = link.string
        print (title)


trade_spider(gumtree)


