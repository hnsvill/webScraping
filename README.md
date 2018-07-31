# webScraping
Getting some web scraping scripts for a friend's project

AlphabetSoup.py cointains the main crawler.

The spider starts by going to the A universes then getting all the links and storing them in an array.
the spider visits all the links in the array. If there are even more series listed here, another array is created and those links are stored.

Now that all of the links that will contain the series data are gathered, each site will be visited and each item's related text written to an excel file. While this is happening, robot parser is being checked and waits are called.