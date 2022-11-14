from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("D:\F Drive\ZeApp\Python web scraping\Buy Shangri-La Online _ Kogan.com.html")
#driver.get("https://www.kogan.com/au/lacie/?page=3")

time.sleep(10)
print(driver.title)

maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

print("Total home-entertainment Items : ",len(maindata))



link_list = []

for i,v in enumerate(maindata):


    name =  driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']/div[1]/div[1]/h2/a")
    try :
        if name[i] is not None:
            print(name[i].get_attribute('href'))
            link_list.append(name[i].get_attribute('href'))
    except:
        print("Not get")
       
    

print(link_list)
