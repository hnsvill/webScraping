#this document is for testing pieces of code

# from creds import credentials

# alphabetSoup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# for alpha in alphabetSoup:
#     print (alpha)

import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.6pm.com/robots.txt")
rp.read()
print ("robot requests rate is: " + str(rp.request_rate("*")))
print ("robot wait rate is: " + str(rp.crawl_delay("*")))
canFet = rp.can_fetch("*", "https://www.6pm.com/women-boots/CK_XARCz1wHAAQHiAgMBAhg.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/&pf_rd_r=S5YJENBEKSQXF5ZX4C4Z&pf_rd_p=4499a5a8-6bcb-4850-a24b-50962ee59fae")
print("Can fetch?: " + str(canFet))