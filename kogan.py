from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#driver.get(" https://www.kogan.com/au/samsung/shop/category/home-entertainment-3762/?page=4")
#driver.get("https://www.kogan.com/au/apple/shop/category/home-entertainment-3762/?page=1")
driver.get("https://www.kogan.com/au/google/shop/category/home-entertainment-3762/?page=1")

time.sleep(40)
print(driver.title)

maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

print("Total home-entertainment Items : ",len(maindata))

cat = driver.find_elements(By.XPATH,"//*[@id='page-content']/div[2]/div[2]/section/div[1]")
print("Category : ",cat[0].text)

link_list = []



# for i,v in enumerate(maindata):
    #print("Item :",i)

    #d1 =  driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']/div[1]/div")
   # print(d1[i].text)

   # print("\n")


for i,v in enumerate(maindata):

    # pic =  driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']/div[1]/figure/a/picture/img")
   #  print(pic[i])

    
    name =  driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']/div[1]/div[1]/h2/a")

    print( link_list)

    print("Item Name : ",name[i].get_attribute('href'))
    link_list.append(name[i].get_attribute('href'))
    
    print("++++")

print(link_list)


#driver.get(Tv_Home_Theature[0])

#print(driver.title)

#maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

#print("Total Item in samsun ",len(maindata))
    

    




