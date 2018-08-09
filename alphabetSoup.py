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
    print (canFet)
    return canFet

def containsString(inSearch, searchFor):
    if searchFor in inSearch:
        return True
    else:
        return False

def getPageLinks(fullUrl):
    sleepytime = random.randint(20,45)
    time.sleep(sleepytime)
    print("sleeping for " + str(sleepytime) + "seconds")
    pageHTML = requests.get(fullUrl)
    convertedText = pageHTML.text
    soup = BeautifulSoup(convertedText, "html.parser")
    for link in soup.find_all("a"):
        if containsString(link.get("href"), "universe?"):
            universePg.append("http://www.figurerealm.com/" + link.get("href"))
        elif containsString(link.get("href"), "actionfigure?") and "http://www.figurerealm.com/" + link.get("href") not in yesScrape:
            yesScrape.append("http://www.figurerealm.com/" + link.get("href"))

robotsPath = "http://www.figurerealm.com/robots.txt"
incUrl = "http://www.figurerealm.com/universe?index="
# alphaSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphaSoup = ["B"]

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
        print(universeLink)
        getPageLinks(universeLink)

print ("universePg = ")
print (universePg)
print ("yesScrape = ")
print (yesScrape)
print ("noScrape = ")
print (noScrape)

emailFromHnsvill("All done!")