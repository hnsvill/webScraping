from bs4 import BeautifulSoup
import requests


def tradeSpider(maxPages):
    page=1
    url = "https://www.6pm.com/women-dresses/CKvXARDE1wHAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&p=" + str(page)
    sourceTxt = requests.get(url)
    plainTxt = sourceTxt.text
    newSoup = BeautifulSoup(plainTxt)
    for namesX in newSoup.find_all("p", {"class": "_3BAWv"}):
        print(namesX)

maxPgs = 2
tradeSpider(maxPgs)