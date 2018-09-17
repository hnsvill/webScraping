from bs4 import BeautifulSoup
from sendEmail import emailFromHnsvill
import requests
import urllib.robotparser
import random
import time
import string

def spiderCanScrape(urlTxt):
    """Returns bool = TRUE if the bot is allowed to scrape the page."""
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("http://www.figurerealm.com/robots.txt")
    rp.read()
    canFet = rp.can_fetch("*", urlTxt)
    return canFet

def cookSoup(definedURL):
    """Returns the page requested as a string."""
    pageHTML = requests.get(definedURL)
    convertedText = pageHTML.text
    return BeautifulSoup(convertedText, "html.parser")

def getPageLinks(fullUrl):
    """Returns the page requested as a string."""
    # time.sleep(random.randint(55,125))  #Delays the requests in order to save the server
    if spiderCanScrape(fullUrl):
        soup = cookSoup(fullUrl)
        for link in soup.find_all("a"):
            linkToFollow = str(link.get("href"))
            if "universe?" in linkToFollow:
                universePg.append("http://www.figurerealm.com/" + linkToFollow)
            elif "actionfigure?" in linkToFollow and "http://www.figurerealm.com/" + linkToFollow not in yesScrape:
                yesScrape.append("http://www.figurerealm.com/" + linkToFollow)
    else:
        noScrape.append("http://www.figurerealm.com/" + fullUrl)

def getUniverseSeries(univURL):
    """Gather lists of URLs to scrape."""
    soup = cookSoup(univURL)
    for linkItem in soup.find_all("td"):
        onclickStrTemp = str(linkItem.get("onclick"))
        startOfOnClick = onclickStrTemp.find("'") + 1
        endOfOnClick = len(onclickStrTemp) - 1
        onclickStr = onclickStrTemp[startOfOnClick:endOfOnClick]
        if "actionfigure?" in onclickStr and "http://www.figurerealm.com/" + onclickStr not in yesScrape:
            yesScrape.append("http://www.figurerealm.com/" + onclickStr)


incUrl = "http://www.figurerealm.com/universe?index=" #main URL pattern, just missing the letter at the end
alphaSoup = list(string.ascii_uppercase)
alphaSoup = ["Y"]

universePg = []
yesScrape = []
noScrape = []

# Get all of the series & universe pages from the directory
for alpha in alphaSoup:
    try:
        if spiderCanScrape(incUrl + alpha):  
            getPageLinks(incUrl + alpha)
            print("tried visiting site")
        else:
            noScrape.append("http://www.figurerealm.com/" + incUrl + alpha)
    except:
        emailFromHnsvill("Something in scraper Went Wrong..")

# The directory has some pages that have universes where there are otherwise series links.
# Now, get the series pages from the universe pages
for universeLink in universePg:
    if spiderCanScrape(universeLink):
        getUniverseSeries(universeLink)

# Go through the series pages, and write each item to an excel file
# for seriesLink in yesScrape:
#     soup = cookSoup(seriesLink)

# Print out links for visual aid before excel file writer works
print ("universePg = ")
print (universePg)
print ("yesScrape = ")
print (yesScrape)
print ("noScrape = ")
print (noScrape)

emailFromHnsvill("All done with Y!")