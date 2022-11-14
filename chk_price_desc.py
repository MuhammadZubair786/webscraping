from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.kogan.com/au/buy/klika-genuine-samsung-smart-tv-remote-control-bn59-01386b-bn59-01386b/")

time.sleep(20)
description  = driver.find_element(By.XPATH,'//div[@class="_3Nf6Y"]').get_attribute('innerHTML')
print(description)

 
