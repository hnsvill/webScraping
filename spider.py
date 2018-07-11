from bs4 import BeautifulSoup
import requests

url = "http://www.6pm.com"
pageHTML = requests.get(url)
convertedText = pageHTML.text
soup = BeautifulSoup(convertedText, "html.parser")

for link in soup.find_all("a", {"class" : "cta gae-click*Gateway-homepage-refresh*ImagesGrid*Shop-All-Brands"}):
    print(link.text)

print(soup.name)

# What I want for this prject, high-level to low-level
# an excel spreadsheet with figurerealm.com data

# a function to verify I'm not on a page that robots.txt says not to scrape
# looking for an way to neatly collect the item and attributes jessica and I put together.