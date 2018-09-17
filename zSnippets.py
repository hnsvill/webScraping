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

def containsString(inSearch, searchFor):
    return searchFor in inSearch
    # if searchFor in inSearch:
    #     return True
    # else:
    #     return False
print(containsString("computer", "cp"))
