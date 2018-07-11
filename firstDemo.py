#starting with selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("Yamaha R6")
elem.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()

print()