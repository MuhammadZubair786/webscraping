from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

import xlsxwriter

from webdriver_manager.chrome import ChromeDriverManager

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Book1.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))







Link=['https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-512gb-black-brand-new-sonx1iv12r512blkprt/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-10-iv-xq-cc72-5g-6gb128gb-daul-sim-black-international-ver-sy-xp10iv-6128-bk/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-10-iv-xq-cc72-5g-6gb128gb-daul-sim-white-international-ver-sy-xp10iv-6128-wh/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb-ram-64gb-rom-as-new-as-new-64gb-bordeaux-red-sonyxperiaxz3rfasnewbred/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-10-iv-dual-sim-5g-6gb-ram-128gb-black-brand-new-sonxp10iv6r128blkprt/',
'https://www.kogan.com/au/buy/threesons-sony-xperia-xz3-64gb-refurbished-excellent-condition-green-sxperiaxz3rfexc64gbgreen/',
'https://www.kogan.com/au/buy/digitalstore-brand-new-sony-xperia-pro-i-dual-sim-5g-12gb-ram-512gb-frosted-black-sy-xperia-pro-i-ds-5g-12-512-blck-bx/',
'https://www.kogan.com/au/buy/threesons-sony-xperia-pro-1-iv-512gb-12gb-5g-dual-brand-new-white-sxperiaiiv512gbbnwhite/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-pro-i-dual-sim-5g-12gb-ram-512gb-frosted-black-brand-new-xpepro-i12r512blkprt/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-10-iv-xq-cc72-5g-6gb128gb-daul-sim-mint-international-ver-sy-xp10iv-6128-gn/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-10-iv-xq-cc72-5g-6gb128gb-daul-sim-lavender-international-ver-sy-xp10iv-6128-pp/',
'https://www.kogan.com/au/buy/spz-sony-xperia-1-iii-xq-bc72-5g-dual-sim-12gb256gb-au-seller-sonyxperia1iii512gbfgray/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb-ram-64gb-rom-as-new-as-new-64gb-black-sonyxperiaxz3rfasnewblack/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-10-iv-dual-sim-5g-6gb-ram-128gb-white-brand-new-sonxp10iv6r128whtprt/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb-ram-64gb-rom-excellent-excellent-64gb-white-sonyxperiaxz364gbrfexcwhite/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-10-iv-dual-sim-5g-6gb-ram-128gb-mint-brand-new-sonxp10iv6r128mntprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-512gb-white-brand-new-sonx1iv12r512whtprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-10-iv-dual-sim-5g-6gb-ram-128gb-lavender-brand-new-sonxp10iv6r128lavprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-black-free-delivery-xper1iii512blkprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-purple-free-delivery-xper1iii512prpprt/',
'https://www.kogan.com/au/buy/threesons-sony-xperia-xz3-64gb-refurbished-as-new-green-sxperiaxz3rfan64gbgreen/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-grey-free-delivery-xper1iii512gryprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-special-price-used-as-demo-sony-xperia-5-j9210-dual-sim-6gb-ram-128gb-blue-usdsonex5dual128gbbl-pink/',
'https://www.kogan.com/au/buy/eclipsetechnology-special-price-used-as-demo-sony-xperia-5-j9210-dual-sim-128gb-6gb-ram-smartphone-grey-usdsonex5dual128gbgry-pink/',
'https://www.kogan.com/au/buy/digitalstore-brand-new-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-black-sy-xp-1-iii-ds-5g-12-512-bk-bx/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-512gb-purple-brand-new-sonx1iv12r512prpprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-black-brand-new-xper1iii512blkprt-vr/',
'https://www.kogan.com/au/buy/eclipsetechnology-special-price-used-as-demo-sony-xperia-pro-i-dual-sim-4g-12gb-ram-512gb-frosted-black-looks-new-5g-not-working-usdsonexproids4g12g512bblk-pink/',
'https://www.kogan.com/au/buy/spz-sony-xperia-10-iv-5g-6gb-ram-128gb-rom-white-sonyxperia10iv5gwhite/',
'https://www.kogan.com/au/buy/spz-sony-xperia-10-iv-5g-6gb-ram-128gb-rom-black-sonyxperia10iv5gblack/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb-ram-64gb-rom-excellent-excellent-64gb-bordeaux-red-sonyxperiaxz3rf64gbexcbred/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-grey-brand-new-xper1iii512gryprt-vr/',
'https://www.kogan.com/au/buy/digitalstore-brand-new-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-purple-sy-xp-1-iii-ds-5g-12-512-pr-bx/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-purple-brand-new-xper1iii512prpprt-vr/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb64gb-rom-refurbished-fair-fair-64gb-black-sonyxperiaxz364gbrefrblack/',
'https://www.kogan.com/au/buy/digitalstore-brand-new-sony-xperia-1-iii-dual-sim-5g-12gb-ram-512gb-frosted-grey-sy-xp-1-iii-ds-5g-12-512-gy-bx/',
'https://www.kogan.com/au/buy/sony-xperia-10-ii-128gb-white-sony/',
'https://www.kogan.com/au/buy/no-frills-electronics-sony-xqd-240gb-memory-card-qdg240f/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-1-iv-xq-ct72-5g-12gb256gb-dual-sim-purple-sy-xp1iv-256-pp/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-1-iv-xq-ct72-5g-12gb512gb-dual-sim-white-sy-xp1iv-512-wh/',
'https://www.kogan.com/au/buy/parkaustralia-sony-xperia-10-iv-5g-6gb128gb-lavender-sn0033/',
'https://www.kogan.com/au/buy/parkaustralia-sony-xperia-10-iv-5g-6gb128gb-green-sn0036/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-1-iv-xq-ct72-5g-12gb512gb-dual-sim-black-sy-xp1iv-512-bk/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-1-iv-xq-ct72-5g-12gb256gb-dual-sim-black-sy-xp1iv-256-bk/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-1-iv-xq-ct72-5g-12gb512gb-dual-sim-purple-sy-xp1iv-512-pp/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-5-iii-5g-xq-bq72-8gb-ram-256gb-rom-dual-sim-black-sy-bq72-256-bk/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-5-iii-5g-xq-bq72-8gb-ram-256gb-rom-dual-sim-green-sy-bq72-256-gn/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-5-iv-8gb256gb-dual-sim-white-xq-cq72-international-ver-sy-xp5iv-8256-wh/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-5-iv-8gb256gb-dual-sim-green-xq-cq72-international-ver-sy-xp5iv-8256-gn/',
'https://www.kogan.com/au/buy/vchain-sony-xperia-1-iv-xq-ct72-5g-dual-sim-12gb-ram-256gb-white-sny-xqct72-256-we/',
'https://www.kogan.com/au/buy/buy-mobile-sony-xperia-1-iv-xq-ct72-12gb-ram-256gb-5g-sne-xq-ct72-1-iv-12-256gb-5g-prp/',
'https://www.kogan.com/au/buy/buy-mobile-sony-xperia-5-iv-xq-cq72-8gb-ram-256gb-5g-sne-5-iv-xq-cq72-8-256gb-5g-grn/',
'https://www.kogan.com/au/buy/buy-mobile-sony-xperia-1-iv-xq-ct72-12gb-ram-512gb-5g-sne-xq-ct72-1-iv-12-512gb-5g-wht/',
'https://www.kogan.com/au/buy/buy-mobile-sony-xperia-10-iv-xq-cc72-6gb-ram-128gb-5g-sne-xq-cc72-10-iv-6-128gb-5g-mnt/',
'https://www.kogan.com/au/buy/no-frills-electronics-sony-xqd-64gb-memory-card-qdg64f/',
'https://www.kogan.com/au/buy/no-frills-electronics-sony-xqd-120gb-memory-card-qdg120f/',
'https://www.kogan.com/au/buy/heybattery-sony-xperia-5-iv-8gb256gb-dual-sim-black-xq-cq72-international-ver-sy-xp5iv-8256-bk/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-256gb-purple-brand-new-sonx1iv12r256prpprt/',
'https://www.kogan.com/au/buy/threesons-sony-xperia-pro-1-iv-512gb-12gb-5g-dual-brand-new-black-sxperiaiiv512gbbnblack/',
'https://www.kogan.com/au/buy/spz-sony-xperia-xz3-4gb-ram-64gb-rom-excellent-excellent-64gb-black-sonyxperiaxz364gbrfexcblack/',
'https://www.kogan.com/au/buy/aualg-sony-xperia-5-64gb-silver-very-good-condition-sonxpr564slvc/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-256gb-black-brand-new-sonx1iv12r256blkprt/',
'https://www.kogan.com/au/buy/eclipsetechnology-sony-xperia-1-iv-12gb-ram-256gb-white-brand-new-sonx1iv12r256whtprt/',
'https://www.kogan.com/au/buy/oz-digital-online-new-sony-xperia-xz-f8332-dual-sim-4g-64gb-platinum-lte-23mp-52-unlocked-phone-01220-00280-00/',
'https://www.kogan.com/au/buy/oz-digital-online-new-sony-xperia-5-dual-j9210-128gb-red-6gb-unlocked-phone-1-year-au-wty-01220-00390-00/',
'https://www.kogan.com/au/buy/unique-deals-unlocked-sony-xperia-e-c1504-sleek-3g-wifi-hotspot-gps-android-cheap-easy-use-7311271419297/',
'https://www.kogan.com/au/buy/oz-digital-online-new-sony-xperia-5-ii-dual-5g-256gb-xq-as72-black-8gb-unlocked-phone-1-yrauwty-01220-00398-00/',
'https://www.kogan.com/au/buy/oz-digital-online-new-sony-xperia-z5-premium-e6883-dual-4g-32gb-gold-unlocked-phone-1-yr-au-wty-01220-00227-00/']


for i ,value  in enumerate(Link):

    driver.get(Link[i])
    if i==0:
        time.sleep(12)
    time.sleep(10)
   



    # name

    worksheet.write(i+1, 0 , Link[i])

    try:

        cat = driver.find_elements(By.XPATH,'//*[@id="product-detail-header"]')
        print("Category : ",cat[0].text)

        worksheet.write(i+1, 1 ,cat[0].text)


        try:

            name = driver.find_elements(By.XPATH,"//*[@id='page-content']/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/h1")
           # # print(name[0].text)

            worksheet.write(i+1, 2 , name[0].text)

            worksheet.write(i+1, 8 , "sony")

            description  = driver.find_element(By.XPATH,'//div[@class="_3Nf6Y"]').get_attribute('innerHTML')
           # # print(description)

            worksheet.write(i+1, 9, description)

            try:
                
                image = driver.find_element(By.XPATH,'//*[@class="image-gallery-image"]').get_attribute('src')
                # # print(image)

                worksheet.write(i+1, 3, image)

                try :
                    
                    price = driver.find_element(By.XPATH,'//div[@class="_3P2BM"]/span')
                   # # print(price.text)

                    worksheet.write(i+1, 4, price.text)

                    try:
                        price2 = driver.find_element(By.XPATH,'//span[@class="_2tkSX"]')
                      #  # print(price2.text)

                        worksheet.write(i+1, 5, price2.text)

                        try :

                            model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                            # print(model.text)

                            worksheet.write(i+1, 6, model.text)

                            try:

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(prop.text)

                                worksheet.write(i+1, 7, prop.text)
                                
                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")
                                

                        except:
                            # print("No MPN VALUE")
                            worksheet.write(i+1, 6, "No MPN VALUE")

                            try:

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(props.text)

                                worksheet.write(i+1, 7, props.text)
                                
                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")

                            
                            
                        
                        
                    except:
                        
                        # print("old Price not get")
                        worksheet.write(i+1, 5, "NO PRICE")
                        
                        try :
                            
                            model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                            # print(model.text)

                            worksheet.write(i+1, 6, model.text)

                            try:
                                
                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(prop.text)

                                worksheet.write(i+1, 7, prop.text)

                                

                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")
                                
                            
                        except:
                            
                            # print("No MPN VALUE")
                            worksheet.write(i+1, 6, "No MPN VALUE")

                            try :

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(props.text)

                                worksheet.write(i+1, 7, props.text)

                               
                                   

                              
                                    

                                    


                                    
                                
                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")
                        
                        

                        
                    
                except:
                    # print("Sold Out")
                    worksheet.write(i+1, 4, "No price")

                    try :
                            
                        model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                        # print(model.text)

                        worksheet.write(i+1, 6, model.text)

                        try:
                                
                            prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                            # print(prop.text)

                            worksheet.write(i+1, 7, prop.text)

                                

                        except:
                            # print("No UPC VALUE")
                            worksheet.write(i+1, 5, "No UPC VALUE")
                                
                            
                    except:
                            
                        # print("No MPN VALUE")
                        worksheet.write(i+1, 6, "No MPN VALUE")
                    
                    
                
            except :

                # print("Image Link not")
                worksheet.write(i+1, 3, "No image")
            
                
            
        except:
            # print("NAME NOT GET")
            worksheet.write(1, 2, "No name")

    except:
        try:

            name = driver.find_elements(By.XPATH,"//*[@id='page-content']/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/h1")
            # print(name[0].text)

            worksheet.write(i+1, 2 , name[0].text)

            worksheet.write(i+1, 8 , "sony")

            description  = driver.find_element(By.XPATH,'//div[@class="_3Nf6Y"]')
            # print(description.text)

            worksheet.write(i+1, 9, description.text)

            try:
                
                image = driver.find_element(By.XPATH,'//*[@class="image-gallery-image"]').get_attribute('src')
                # print(image)

                worksheet.write(i+1, 3, image)

                try :
                    
                    price = driver.find_element(By.XPATH,'//div[@class="_3P2BM"]/span')
                    # print(price.text)

                    worksheet.write(i+1, 4, price.text)

                    try:
                        price2 = driver.find_element(By.XPATH,'//span[@class="_2tkSX"]')
                        # print(price2.text)

                        worksheet.write(i+1, 5, price2.text)

                        try :

                            model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                            # print(model.text)

                            worksheet.write(i+1, 6, model.text)

                            try:

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(prop.text)

                                worksheet.write(i+1, 7, prop.text)
                                
                            except:
                                # print("Props not get")
                                worksheet.write(i+1, 7, "No props")
                                

                        except:
                            # print("No MPN VALUE")
                            worksheet.write(i+1, 6, "No MPN VALUE")

                            try:

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(props.text)

                                worksheet.write(i+1, 7, props.text)
                                
                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")

                            
                            
                        
                        
                    except:
                        
                        # print("No Price")
                        worksheet.write(i+1, 5, "No Price")
                        
                        try :
                            
                            model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                            # print(model.text)

                            worksheet.write(i+1, 6, model.text)

                            try:
                                
                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(prop.text)

                                worksheet.write(i+1, 7, prop.text)

                                

                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")
                                
                            
                        except:
                            
                            # print("No MPN VALUE")
                            worksheet.write(i+1, 6, "No MPN VALUE")

                            try :

                                prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                                # print(props.text)

                                worksheet.write(i+1, 7, props.text)

                               
                                   

                              
                                    

                                    


                                    
                                
                            except:
                                # print("No UPC VALUE")
                                worksheet.write(i+1, 7, "No UPC VALUE")
                        
                        

                        
                    
                except:
                    # print("No price")
                    worksheet.write(i+1, 4, "No price")

                    try :
                            
                        model = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[1]')
                        # print(model.text)

                        worksheet.write(i+1, 6, model.text)

                        try:
                                
                            prop  = driver.find_element(By.XPATH,'//div[@class="_1WvMC"]/p[2]')
                            # print(prop.text)

                            worksheet.write(i+1, 7, prop.text)

                                

                        except:
                            # print("No UPC VALUE")
                            worksheet.write(i+1, 7, "No UPC VALUE")\
                                                     
                                
                            
                    except:
                            
                        # print("No MPN VALUE")
                        worksheet.write(i+1, 6, "No MPN VALUE")
                    
                    
                
            except :

                # print("Image Not get")
                worksheet.write(i+1, 3, "No image")
            
                
            
        except:
            # print("NAME NOT GET")
            worksheet.write(1, 2, "No name")
        

workbook.close()
       
        
