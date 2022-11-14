from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.ui as UI
import time

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("D:\F Drive\ZeApp\Python web scraping\Buy Stanley Tools & Automotive Online _ Kogan.com.html")
time.sleep(10)

print("Title : " , driver.title)

itemCount = 0



print("Title : " , driver.title)

maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

print("Total Products ",len(maindata))

itemCount +=len(maindata)
print("\n")


print("Total Tools_Automotive  PRODUCTS :  ",itemCount)




