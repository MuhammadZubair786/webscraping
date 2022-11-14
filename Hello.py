from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)


Url_List =[
    'https://www.flashscore.com/football/europe/europa-league/fixtures/',
    'https://www.flashscore.com/football/spain/laliga/',
    ]


for index, item in  enumerate(Url_List) :
    
    url = item
    driver.get(url)
    print(driver.title)

    maindata = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']")


    print(len(maindata))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    print(str(index)+")"+ driver.title)

    for i,v in enumerate(maindata):

        time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[2]")

        team1 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[3]")

        team2 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[4]")

        print(time[i].text + "  " + team1[i].text + " VS " +team2[i].text)
