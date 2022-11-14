from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)


url="https://www.flashscore.com/football/europe/europa-league/fixtures/"
driver.get(url)
print(driver.title)

data = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']")

print(len(data))




    
    
   

