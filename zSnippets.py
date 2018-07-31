#this document is for testing pieces of code

def roboParse():
    import urllib.robotparser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("https://www.6pm.com/robots.txt")
    rp.read()
    print ("robot requests rate is: " + str(rp.request_rate("*")))
    print ("robot wait rate is: " + str(rp.crawl_delay("*")))
    canFet = rp.can_fetch("*", "https://www.6pm.com/women-boots/CK_XARCz1wHAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&pf_rd_r=S5YJENBEKSQXF5ZX4C4Z&pf_rd_p=4499a5a8-6bcb-4850-a24b-50962ee59fae")
    print("Can fetch?: " + str(canFet))

def getLetterCol(iColx):
    # alphabetSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return iColx % 2

# print (getLetterCol(5))

def canScrape(robotTxtFileURL, urlTxt):
    import urllib.robotparser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotTxtFileURL)
    rp.read()
    canFet = rp.can_fetch("*", urlTxt)
    print(canFet)

# canScrape("https://www.6pm.com/robots.txt", "https://www.6pm.com/women-boots/CK_XARCz1wHAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&pf_rd_r=S5YJENBEKSQXF5ZX4C4Z&pf_rd_p=4499a5a8-6bcb-4850-a24b-50962ee59fae")

def testParent():
    from bs4 import BeautifulSoup
    import requests
    incUrl = "http://www.figurerealm.com/universe?index=A"
    pageHTML = requests.get(incUrl)
    convertedText = pageHTML.text
    soup = BeautifulSoup(convertedText, "html.parser")
    pgLinks = []
    for link in soup.find_all("a"):

        pgLinks.append(link.get("href"))
        print (link.get("href"))
    print (pgLinks)

# import random
# import time
# import datetime

# for h in range(1,10):
#     print("Something")
#     time.sleep(2)
# # print ("Sleeping at: " + str(datetime.datetime.now()))
# for i in range(1,10):
#     print(random.randint(1,10))
#     time.sleep(random.randint(1,5))
# yourNm = "Hannah"
# print ("Hello, " + yourNm)

# testParent()

# from alphabetSoup import spiderCanScrape

# robotsPath = "http://www.figurerealm.com/robots.txt"
# incUrl = "http://www.figurerealm.com/universe?index="

# print(spiderCanScrape(robotsPath, incUrl + "A"))

def retTry(arg):
    if arg == "opt1":
        return True
    else:
        return False

# print(retTry("Option2"))

if retTry("opt1") == True:
    print("evaluated successfully")
else:
    print("did not eval")