from bs4 import BeautifulSoup
import requests

incUrl = "http://www.figurerealm.com/actionfigure?action=seriesitemlist&id=376&figures=alienresurrection"

# turn the page into text so the parser can read it
pageHTML = requests.get(incUrl)
convertedText = pageHTML.text
soup = BeautifulSoup(convertedText, "html.parser")

# navigate the tree newSoup.find_all("p", {"class": "_3BAWv"}):
for elem in soup.find_all("div", attrs={"group":"checkitem"}):
    for child in elem.children:
        print(child.text)
    
    # for tm in elem.children
    #     print(children)
    # # print(elem.contents)

print(soup.name + " " + "Success!")
