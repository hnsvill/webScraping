import urllib.robotparser

webUrl = "http://www.musi-cal.com"
rp = urllib.robotparser.RobotFileParser()

rp.set_url(webUrl + "/robots.txt")
rp.read()
rrate = rp.request_rate("*")
rrate.requests
rrate.seconds
rp.crawl_delay("*")

rp.can_fetch("*", webUrl + "/cgi-bin/search?city=San+Francisco")

rp.can_fetch("*", webUrl + "/")