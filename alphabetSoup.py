from bs4 import BeautifulSoup
import requests

incUrl = "http://www.figurerealm.com/universe?index="

alphabetSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for alpha in alphabetSoup:
    pageHTML = requests.get(incUrl)
    convertedText = pageHTML.text
    soup = BeautifulSoup(convertedText, "html.parser")


for link in soup.find_all("span", {"class" : "button round5 shade2"}):
    print(onclick)

print(soup.name + " " + "Success!")

# What I want for this prject, high-level to low-level
# an excel spreadsheet with figurerealm.com data

# a function to verify I'm not on a page that robots.txt says not to scrape
# loo king for an way to neatly collect the item and attributes jessica and I put together.


# Loop through entire alpabet
# "http://www.figurerealm.com/universe?index=" + "A"