from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)


Url_List =[
    'https://www.flashscore.com/football/europe/champions-league/',
    'https://www.flashscore.com/football/europe/europa-league/fixtures/',
    'https://www.flashscore.com/football/spain/laliga/',
    'https://www.flashscore.com/football/england/premier-league/fixtures/',
    'https://www.flashscore.com/football/germany/bundesliga/fixtures/',
    'https://www.flashscore.com/football/france/ligue-1/fixtures/',
            ]


df=open('text file.txt','a')
df.write("All Leagues Matches Schuldes : "+"\n\n")

for index, item in enumerate(Url_List):
    

    url=item
    driver.get(url)
  
    chktitle = driver.title
    ind = chktitle.find("Fixture")

    if(ind==-1):
        print(chktitle[0:17])
        df.write("\n"+str(index+1)+" ) "+  chktitle[0:17]+"\n\n")
    else:
        print(chktitle[0:ind])
        df.write("\n"+str(index+1)+" ) "+  chktitle[0:ind]+"\n\n")


    maindata = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']")

    for i,v in enumerate(maindata):

        time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[1]")
        

        if(len(time[i].text)!=0):

            
            time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[1]")
            team1 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[2]")
            team2 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[3]")

            print(time[i].text + "  " + team1[i].text + " VS " +team2[i].text)
            df.write(time[i].text + "  " + team1[i].text + " VS " +team2[i].text+"\n")
            

        else:

            time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[2]")
            team1 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[3]")
            team2 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--twoLine']/div[4]")

            print(time[i].text + "  " + team1[i].text + " VS " +team2[i].text)
            df.write(time[i].text + "  " + team1[i].text + " VS " +team2[i].text+"\n")
            

    last_match = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']")
    

    for j,val in enumerate(last_match):

        time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[1]")


        if(len(time[j].text)!=0):
            
            time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[1]")
            team1 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[2]")
            team2 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[3]")

            df.write(time[j].text + "  " + team1[j].text + " VS " +team2[j].text+"\n")
            print(time[j].text + "  " + team1[j].text + " VS " +team2[j].text)

        else:
            
            time = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[2]")
            team1 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[3]")
            team2 = driver.find_elements(By.XPATH,"//div[@class='event__match event__match--static event__match--scheduled event__match--last event__match--twoLine']/div[4]")

            df.write(time[j].text + "  " + team1[j].text + " VS " +team2[j].text+"\n") 
            print(time[j].text + "  " + team1[j].text + " VS " +team2[j].text)
            

df.close()
driver.close()
        
