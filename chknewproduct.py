from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.ui as UI
import time

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://www.kogan.com/au/buy/digitalstore-apple-iphone-11-64gb-any-colour-excellent-grade-apple-iphone-11-64gb-any-exl-g/")
time.sleep(20)

print("Title : " , driver.title)

itemCount = 0



print("Title : " , driver.title)

maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

print("Total Products ",len(maindata))

itemCount +=len(maindata)
print("\n")


print("Total Tools_Automotive  PRODUCTS :  ",itemCount)
