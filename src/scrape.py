# scrape balance sheets
from bs4 import BeautifulSoup
import requests
from pprint import pprint
# import lxml
from lxml import html, etree
from urllib.request import urlopen
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def scrape(ticker):
    # https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA

    url = 'https://www.google.com/'
    page = requests.get(url)
    print(page.content)
    tree = html.fromstring(page.content)
    # print(tree)
    xpath = "/html/body"
    data = tree.xpath(xpath)
    print(data[0].text)
    # print(data)


    

    # baseURL = "https://finance.yahoo.com/quote/TSLA/balance-sheet?p="
    # requestURL = baseURL + ticker

    # page = requests.get(requestURL).content

    # # # pprint(page.content.decode('UTF-8'))
    # # soup = BeautifulSoup(page.content, 'html.parser')
    # # # pprint(soup)

    # # page = urlopen(requestURL)
    # # print(page.read())
    # # page.read()
    # # parser = etree.HTMLParser()
    # doc = lxml.etree.fromstring(page)
    # doctree = etree.parse(page, parser)
    # print(doc.xpath("//*[@id='Col1-1-Financials-Proxy']/section/div[2]/h3/span/text()"))