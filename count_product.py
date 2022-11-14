from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:\Program Files (x86)/chromedriver.exe')
driver = webdriver.Chrome(service=s)

Tv_Home_Theature = [
    'https://www.kogan.com/au/samsung/shop/category/home-entertainment-3762/?page=4',
    'https://www.kogan.com/au/apple/shop/category/home-entertainment-3762/?page=5',
    'https://www.kogan.com/au/google/shop/category/home-entertainment-3762/?page=1',
    'https://www.kogan.com/au/philips/shop/category/home-entertainment-3762/?page=16',
    'https://www.kogan.com/au/sony/shop/category/home-entertainment-3762/?page=2',
    'https://www.kogan.com/au/lg/shop/category/home-entertainment-3762/',
    'https://www.kogan.com/au/panasonic/shop/category/home-entertainment-3762/?page=2',
    'https://www.kogan.com/au/pioneer/shop/category/home-entertainment-3762/',
    "https://www.kogan.com/au/yamaha/?page=12"
    ]


Phones_Tablets_Wearables = [
    'https://www.kogan.com/au/apple/c/phones-tablets-wearables/?page=50',
    'https://www.kogan.com/au/samsung/c/phones-tablets-wearables/?page=50',
    'https://www.kogan.com/au/oneplus/c/phones-tablets-wearables/?page=10',
    'https://www.kogan.com/au/google/c/phones-tablets-wearables/?page=12',
    'https://www.kogan.com/au/garmin/c/phones-tablets-wearables/?page=10',
    'https://www.kogan.com/au/sony/c/phones-tablets-wearables/?page=10',
    'https://www.kogan.com/au/xiaomi/c/phones-tablets-wearables/?page=12'
    ]


Computer_Laptop_Gaming =[
    'https://www.kogan.com/au/lenovo/c/computers-laptops-gaming/?page=50',
    'https://www.kogan.com/au/apple/c/computers-laptops-gaming/?page=30',
    'https://www.kogan.com/au/samsung/c/computers-laptops-gaming/?page=50',
    'https://www.kogan.com/au/microsoft/c/computers-laptops-gaming/?page=10',
    'https://www.kogan.com/au/hp/c/computers-laptops-gaming/?page=46',
    'https://www.kogan.com/au/lg/c/computers-laptops-gaming/?page=7',
    'https://www.kogan.com/au/google/c/computers-laptops-gaming/',
    'https://www.kogan.com/au/xbox/c/computers-laptops-gaming/?page=2',
    'https://www.kogan.com/au/playstation/c/computers-laptops-gaming/?kogan_first=true&page=3',
    'https://www.kogan.com/au/nintendo/c/computers-laptops-gaming/?page=10',
    'https://www.kogan.com/au/gorilla-gaming/c/computers-laptops-gaming/'
    
    ]

Electronic = [
    'https://www.kogan.com/au/canon/shop/category/electronics-2920/',
    'https://www.kogan.com/au/nikon/shop/category/electronics-2920/',
    'https://www.kogan.com/au/dji/shop/category/electronics-2920/',
    'https://www.kogan.com/au/arlo/shop/category/electronics-2920/',
    "https://www.kogan.com/au/swann/shop/category/electronics-2920/?page=4",
    'https://www.kogan.com/au/fujifilm/shop/category/electronics-2920/',
    'https://www.kogan.com/au/apple/shop/category/electronics-2920/?page=4',
    'https://www.kogan.com/au/ultimate-ears/shop/category/electronics-2920/',
    'https://www.kogan.com/au/lacie/?page=3',
    'https://www.kogan.com/au/oculus/shop/category/electronics-2920/'
    ]

Smart_Home=[
    "https://www.kogan.com/au/philips/c/smart-home/?page=3",
    "https://www.kogan.com/au/apple/c/smart-home/",
    "https://www.kogan.com/au/amazon/c/smart-home/",
    "https://www.kogan.com/au/google/c/smart-home/?page=2",
    "https://www.kogan.com/au/lifx/c/smart-home/?page=1",
    "https://www.kogan.com/au/ring/c/smart-home/?page=2",
    ]



Appliances_Whitegoods=[
    "https://www.kogan.com/au/delonghi/shop/home-appliances/?page=2",
    "https://www.kogan.com/au/sunbeam/shop/home-appliances/?page=3",
    "https://www.kogan.com/au/kitchenaid/shop/home-appliances/?page=4",
    "https://www.kogan.com/au/dyson/shop/home-appliances/?page=6",
    "https://www.kogan.com/au/xiaomi/shop/home-appliances/?page=2",
    "https://www.kogan.com/au/roborock/shop/home-appliances/?page=4",
    "https://www.kogan.com/au/gaggia/shop/home-appliances/",
    'https://www.kogan.com/au/devanti/shop/home-appliances/?page=5',
    'https://www.kogan.com/au/healthy-choice/shop/home-appliances/?page=3',
    'https://www.kogan.com/au/irobot/shop/home-appliances/?page=2',
    
    ]


Home_Garden =[
    "https://www.kogan.com/au/ergolux/shop/category/home-garden-3804/?page=4",
    'https://www.kogan.com/au/ovela/shop/category/home-garden-3804/?page=10',
    'https://www.kogan.com/au/matt-blatt/shop/category/home-garden-3804/?page=13',
    'https://www.kogan.com/au/trafalgar/shop/category/home-garden-3804/?page=10',
    'https://www.kogan.com/au/certa/shop/category/home-garden-3804/?page=5',
    'https://www.kogan.com/au/shangri-la/shop/category/home-garden-3804/?page=10',
    'https://www.kogan.com/au/royal-comfort/shop/category/home-garden-3804/?page=12'
    ]


Toys_Hobbies=[
    "https://www.kogan.com/au/shop/category/toys-hobbies-10279/?page=25"
    ]

Sports_Outdoors_Travel=[
    'https://www.kogan.com/au/fortis/shop/sports-outdoors/?page=10',
    'https://www.kogan.com/au/komodo/shop/sports-outdoors/?page=10',
    'https://www.kogan.com/au/american-tourister/shop/sports-outdoors/',
    'https://www.kogan.com/au/garmin/shop/sports-outdoors/?page=14',
    'https://www.kogan.com/au/xiaomi/shop/sports-outdoors/',
    'https://www.kogan.com/au/caribee/shop/sports-outdoors/?page=4',
    'https://www.kogan.com/au/everlast/shop/sports-outdoors/?page=5',
    'https://www.kogan.com/au/manduka/shop/sports-outdoors/?page=2',
    
    
    ]

Tools_Automotive = [
    "https://www.kogan.com/au/certa/shop/tools-automotive/?page=3",
    "https://www.kogan.com/au/rok/shop/tools-automotive/?page=2",
    "https://www.kogan.com/au/komodo/shop/tools-automotive/",
    "https://www.kogan.com/au/stanley/shop/tools-automotive/?page=10",
    "https://www.kogan.com/au/daytek/shop/tools-automotive/",
    "https://www.kogan.com/au/garmin/shop/tools-automotive/?page=6",
    ]



itemCount = 0

for i,v in enumerate(Tools_Automotive ):
    

    driver.get(Tools_Automotive [i])
    if i==0 : 
        time.sleep(40)

    print("Title : " , driver.title)

    maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

    print("Total Products ",len(maindata))

    itemCount +=len(maindata)
    print("\n")


print("Total Tools_Automotive  PRODUCTS :  ",itemCount)




