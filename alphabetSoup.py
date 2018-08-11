from bs4 import BeautifulSoup
from sendEmail import emailFromHnsvill
import requests
import urllib.robotparser
import random
import time

def spiderCanScrape(robotTxtFileURL, urlTxt):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotTxtFileURL)
    rp.read()
    canFet = rp.can_fetch("*", urlTxt)
    return canFet

def containsString(inSearch, searchFor):
    if searchFor in inSearch:
        return True
    else:
        return False

def cookSoup(definedURL):
    pageHTML = requests.get(definedURL)
    convertedText = pageHTML.text
    return BeautifulSoup(convertedText, "html.parser")

def getPageLinks(fullUrl):
    # # # time.sleep(random.randint(55,125))
    soup = cookSoup(fullUrl)
    for link in soup.find_all("a"):
        if containsString(link.get("href"), "universe?"):
            universePg.append("http://www.figurerealm.com/" + link.get("href"))
        elif containsString(link.get("href"), "actionfigure?") and "http://www.figurerealm.com/" + link.get("href") not in yesScrape:
            yesScrape.append("http://www.figurerealm.com/" + link.get("href"))

def getUniverseSeries(univURL):
    soup = cookSoup(univURL)
    for linkItem in soup.find_all("td"):
        onclickStrTemp = str(linkItem.get("onclick"))
        startOfOnClick = onclickStrTemp.find("'") + 1
        endOfOnClick = len(onclickStrTemp) - 1
        onclickStr = onclickStrTemp[startOfOnClick:endOfOnClick]
        if containsString(onclickStr, "actionfigure?") and "http://www.figurerealm.com/" + onclickStr not in yesScrape:
            yesScrape.append("http://www.figurerealm.com/" + onclickStr)

robotsPath = "http://www.figurerealm.com/robots.txt"
incUrl = "http://www.figurerealm.com/universe?index="
# alphaSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphaSoup = ["Y"]

universePg = []
yesScrape = []
noScrape = []

for alpha in alphaSoup:
    try:
        if spiderCanScrape(robotsPath, incUrl + alpha):  
            getPageLinks(incUrl + alpha)
            print("tried visiting site")
        else:
            noScrape.append("http://www.figurerealm.com/" + incUrl + alpha)
    except:
        emailFromHnsvill("Something in scraper Went Wrong..")

for universeLink in universePg:
    if spiderCanScrape(robotsPath, universeLink):
        getUniverseSeries(universeLink)

print ("universePg = ")
print (universePg)
print ("yesScrape = ")
print (yesScrape)
print ("noScrape = ")
print (noScrape)

emailFromHnsvill("All done with Y!")