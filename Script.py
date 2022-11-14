from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#Url_List =[
 #   'https://www.flashscore.com/football/europe/europa-league/fixtures/',
  #  'https://www.flashscore.com/football/england/premier-league/fixtures/',
   # 'https://www.flashscore.com/football/germany/bundesliga/fixtures/',
    #'https://www.flashscore.com/football/france/ligue-1/fixtures/',
    #'https://www.flashscore.com/football/spain/laliga/',
    #]


for index, item in enumerate(Url_List):
    

    url=item
    driver.get(url)
    print(driver.title)

    # data = driver.find_elements(By.CLASS_NAME, "event__match")
    data = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']")

    print(len(data))

    df=open('text file.txt','a')
    if(index==0):
        df.write("Leagues Maatch Schuldes : "+"\n\n")
    df.write(str(index+1)+")"+ str(driver.title)+"\n"+"+++++++++++++++++++++++++++++++++++"+"\n")


    for i in data:
        print(i.text)
        df.write(i.text+"\n")
    

df.close()

driver.close()
# print(data.text)
# print(data.innerHtml)
# print(data.innerText)





