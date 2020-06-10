# scrape balance sheets
from bs4 import BeautifulSoup
import requests
from pprint import pprint
# import lxml
# from lxml import html, etree
# import urllib2
import csv
from urllib.request import urlopen
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

def scrape(ticker):
    # https://finance.yahoo.com/quote/TSLA/balance-sheet?p=TSLA

    headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0 '}
    page = requests.get("https://www.wsj.com/market-data/quotes/" + ticker + "/financials/annual/balance-sheet", headers=headers)
    # pprint(page.content)
    soup = BeautifulSoup(page.content, "html.parser")


    table = soup.select_one(".cr_dataTable")
    table_body = table.select_one("tbody")
    headers = []
    for th in table.find_all("th"):
        headers.append(th.text.strip())
    # print(headers)


    ### https://stackoverflow.com/questions/51685551/beautifulsoup-get-text-of-all-tds-some-text-with-commas-inside-trs


    rows = [headers]
    for tr in table_body.find_all("tr"):
        if len(tr.get("class")) == 0:

            row = [td.text.strip() for td in tr.select('td') if td.text.strip() and td.text.strip() != '-']
            if row:
                rows.append(row)
            # if tr.get("class")[0] != "hide":
            # print(tr.text.strip())
            # td = tr.select_one("td")
            # print(td.text.strip())

    
    print(rows)

    with open('deliverables/download.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    # rows = []
    # for tr in table.find_all("tr")[1:]:
    #     cells = []
    #     # grab all td tags in this table row
    #     tds = tr.find_all("td")
    #     if len(tds) == 0:
    #         # if no td tags, search for th tags
    #         # can be found especially in wikipedia tables below the table
    #         ths = tr.find_all("th")
    #         for th in ths:
    #             cells.append(th.text.strip())
    #     else:
    #         # use regular td tags
    #         for td in tds:
    #             cells.append(td.text.strip())
    #     rows.append(cells)

    # print(rows)

    # save_html(r.content, 'google_com')

    # table_body=soup.find('tbody')
    # rows = table_body.find_all('tr')
    # for row in rows:
    #     cols=row.find_all('td')
    #     cols=[x.text.strip() for x in cols]
    #     print(cols)

    # print("\n\n\n\n\n\n\nasdfasdfasdf\n\n\n\n\n\n\n\n\n\n\n\n\n", soup.select("title"), flush=True)

    # print("aaaaaaa\n\n\n\n\n")
    # for link in soup.find_all('td'):
    #     print(link.text)

    # name_box = soup.find("td", attrs={"class": "indent"})
    # name = name_box.text.strip()
    # print(name)


    # url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'
    # page = requests.get(url)
    # print(page.content)
    # tree = html.fromstring(page.content)
    # xpath = "/html/body/div[2]/section[2]/div/div[2]/div/div[2]/div[2]/table/tbody"
    # data = tree.xpath(xpath)
    # print(data[0].text)
    # # print(data)


    

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