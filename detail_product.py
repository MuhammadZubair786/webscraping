from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#s=Service('C:\Program Files (x86)/chromedriver.exe')
#driver = webdriver.Chrome(service=s)

#driver.get(" https://www.kogan.com/au/samsung/shop/category/home-entertainment-3762/?page=1")

#time.sleep(40)
#print(driver.title)

#maindata = driver.find_elements(By.XPATH,"//div[@class='rs-infinite-scroll _1G8Jr']/div[@class='_3dbuB _2TkM7 _1tVxb tVqMg']")

#print("Total home-entertainment Items : ",len(maindata))

#cat = driver.find_elements(By.XPATH,"//*[@id='page-content']/div[2]/div[2]/section/div[1]")
#print("Category : ",cat[0].text)

samsung_home_entertainment_link_list =['https://www.kogan.com/au/buy/stax-online-samsung-55-bu8000-crystal-uhd-4k-smart-tv-ua55bu8000wxxy-ua55bu8000wxxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-914ch-q-series-soundbar-hw-q930bxy-wireless-true-dolby-atmos-hw-q930b-xy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-65-8-series-led-4k-tv-42415687794847/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01298d-bn59-01298d/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-85-q60a-4k-uhd-qled-smart-hd-tv-led-bluetoothhmdi-television-black-qa85q60aawxxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-75-q80b-qled-4k-tv-42415691366559/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-55-qled-4k-smart-tv-q60a-w-wifiappsbluetoothscreen-cast-slim-look-qa55q60aawxxy/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-2021-slim-wall-mount-43-85-bracket-for-tv-q-seriescrystal-uhd-series-wmn-a50eb-xy/',
           'https://www.kogan.com/au/buy/acosecommerce-replacement-remote-control-for-samsung-aa5900602a-aa59-00602a-smart-tv-led-k-dks-samsng-contrl-z/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01357c-bn59-01357c/',
           'https://www.kogan.com/au/buy/samsung-tv-replacement-remote-control-bn59-01198q-bn59-01198q/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-50-bu8000-crystal-uhd-4k-smart-tv-led-wappbluetoothinternet-browsing-ua50bu8000wxxy/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01309b-bn59-01309b/',
           'https://www.kogan.com/au/buy/klika-genuine-samsung-smart-tv-remote-control-bn59-01386b-bn59-01386b/',
           'https://www.kogan.com/au/buy/samsung-tv-replacement-remote-control-bn59-01175n-bn59-01175n/',
           'https://www.kogan.com/au/buy/genuine-samsung-aa59-00741a-smart-touch-tv-remote-control-aa59-00741a/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01311f-bn59-01311f/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01330q-bn59-01330q/',
           'https://www.kogan.com/au/buy/klika-genuine-samsung-bn59-01385b-smart-tv-remote-control-bn59-01385b/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01312t-bn59-01312t/',
           'https://www.kogan.com/au/buy/genuine-samsung-bn59-01270a-tv-remote-control-bn59-01270a/',
           'https://www.kogan.com/au/buy/genuine-samsung-bn59-01298g-bn59-01298l-tv-remote-control-bn59-01298g/',
           'https://www.kogan.com/au/buy/samsung-tv-replacement-remote-control-bn59-01247a-bn59-01247a/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01363c-bn59-01363c/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01330m-bn59-01330m/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-85-q80b-qled-4k-tv-42415694938271/',
           'https://www.kogan.com/au/buy/acosecommerce-replacement-remote-control-for-samsung-aa5900602a-aa59-00602a-smart-tv-led-k3-dks-samsng-contrl/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-75-qn85b-neo-qled-tv-42415691399327/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-43-8-series-led-4k-tv-42415672033439/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-auto-rotating-stand-mount-for-neo-qled-55-tv-black-home-entertainment-vg-arab43stdxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-55-qn85b-neo-qled-tv-42415682879647/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-65-q80b-qled-4k-tv-42415687827615/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-50-qn90b-neo-qled-tv-42415673671839/',
           'https://www.kogan.com/au/buy/itz-samsung-auto-rotating-motorized-studio-stand-for-selected-samsung-43-55-tv-qn85b-qn90b-frame-ls03b-moasam22002/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-85-qn85b-neo-qled-tv-42415695003807/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-55-q60b-qled-4k-tv-42415682977951/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-32-t5300a-series-fhd-smart-tv-led-1920x1080-w-wi-fi-dolby-hdmiusb-ua32t5300awxxy/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-home-wall-mounted-auto-rotating-accessory-for-5565-neo-qledframe-tv-vg-arab43wmtxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-65-qn85b-neo-qled-tv-42415687860383/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-auto-rotating-wall-mount-for-43-55-neo-qled-the-frame-tv-home-decor-vg-arab22wmtxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-55-q80b-qled-4k-tv-42415682846879/',
           'https://www.kogan.com/au/buy/acosecommerce-replacement-remote-control-for-samsung-aa5900602a-aa59-00602a-smart-tv-led-dks-samsng-contrl/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-43-qn90b-qled-tv-42415672066207/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-65-q60b-qled-4k-tv-42415687958687/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-85-8-series-led-4k-tv-42415694905503/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-fhd-projector-42338807054495/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-65-business-tv-4k-42415688188063/',
           'https://www.kogan.com/au/buy/stax-online-samsung-65-crystal-uhd-4k-smart-tv-ua65bu8000wxxy-ua75bu8000wxxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-75-q60b-qled-smart-tv-qa75q60bawxxy-2022-model-qa75q60bawxxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-b550-21ch-soundbar-42415703752863/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-55-q80a-qled-4k-tv-42415683207327/',
           'https://www.kogan.com/au/buy/kg-superstore-samsung-43-au8000-crystal-4k-uhd-smart-tv-led-3840x2160-w-wi-fi-hdmiusbav-ua43au8000wxxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-50-business-tv-4k-42415673901215/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-43-business-tv-4k-42415672262815/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-hw-q800bxy-soundbar-speaker-black-512-channels-360-w-hw-q800bxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-312ch-q-series-soundbar-hw-q600bxy-wireless-true-dolby-atmos-hw-q600b-xy/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-hw-s801bxy-soundbar-speaker-white-312-channels-hw-s801bxy/',
           'https://www.kogan.com/au/buy/ishoptech-samsung-s61b-50ch-soundbar-42415703621791/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-bea-business-tv-55-uhd-250nits-hdmi2-lan-usb-spkr-167-usage-cms-3yr-lh55beahlgwxxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-b-series-b650-430w-31-channel-soundbar-hw-b650xy-hwb650xy/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-hw-q700bxy-soundbar-speaker-black-312-channels-320-w-hw-q700bxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-85-q60b-qled-4k-smart-tv-qa85q60bawxxy-2022-model-qa85q60bawxxy/',
           'https://www.kogan.com/au/buy/stax-online-samsung-1114ch-q-series-soundbar-hw-q990bxy-wireless-true-dolby-atmos-hw-q990b-xy/',
           'https://www.kogan.com/au/buy/shoptheglobe-samsung-sm-r322nzwaxar-3d-glasses-61-296051951-au/',
           'https://www.kogan.com/au/buy/itz-samsung-lsp9t-the-premiere-triple-laser-4k-smart-projector-with-42-channel-premium-sound-bar-built-in-nz-freeview-tv-dual-tuner-prosam21090/',
           'https://www.kogan.com/au/buy/stax-online-samsung-85-qn800b-neo-qled-8k-smart-tv-2022-qa85qn800bwxxy-qa85qn800bwxxy/',
           'https://www.kogan.com/au/buy/itz-samsung-the-freestyle-full-hd-smart-portable-projector-prosam32230/',
           'https://www.kogan.com/au/buy/onlinedeals-samsung-ultra-slim-tv-wall-mount-bracket-lcd-led-wmn2000a-32-40-tv-wmn2000a/',
           'https://www.kogan.com/au/buy/itz-samsung-full-motion-slim-wall-mount-for-58-75-tv-400x300mm-400x400mm-moasam22012/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-flip-2-wm65r-65in-uhd-interactive-e-boar-lh65wmrwbgcxxy/',
           'https://www.kogan.com/au/buy/itz-samsung-full-motion-slim-wall-mount-for-82-85-tv-600x400mm-moasam22013/',
           'https://www.kogan.com/au/buy/superdeals-samsung-hw-q700axy-hw-q700a-312ch-home-theatre-soundbar-hw-q700axy/',
           'https://www.kogan.com/au/buy/itz-samsung-full-motion-slim-wall-mount-for-43-55-tv-200x200mm-300x200mm-moasam22011/',
           'https://www.kogan.com/au/buy/itz-samsung-slim-fit-tv-wall-mount-compatibility-with-2021-and-2022-year-43-85-excluding-q80-series-wmn-b50ebxy-moasam22010/',
           'https://www.kogan.com/au/buy/stax-online-samsung-b-series-b450-300w-21-channel-soundbar-hw-b450xy-hw-b450xy/',
           'https://www.kogan.com/au/buy/samsung-tv-smart-touch-replacement-remote-control-bn59-01242c-bn59-01242c/',
           'https://www.kogan.com/au/buy/genuine-samsung-bn59-01185b-bn59-01182b-smart-touch-tv-remote-control-bn59-01185b/',
           'https://www.kogan.com/au/buy/best-deal-4-u-computers-samsung-series-8-qa65qn85aawxxy-tv-1651-cm-65-4k-ultra-hd-smart-tv-wi-fi-silver-qa65qn85aawxxy/']


apple_home_entertainment_link_list =['https://www.kogan.com/au/buy/2021-apple-tv-4k-32gb-latest-model/',
            'https://www.kogan.com/au/buy/2021-apple-tv-4k-64gb-latest-model/',
            'https://www.kogan.com/au/buy/mighty-ape-apple-tv-hd-32gb-2021-with-siri-remote-34809944/',
            'https://www.kogan.com/au/buy/mighty-ape-apple-usb-c-digital-av-multiport-adapter-31421567/',
            'https://www.kogan.com/au/buy/mighty-ape-apple-lightning-digital-av-adapter-26772001/',
            'https://www.kogan.com/au/buy/apple-remote-silver-apple/',
            'https://www.kogan.com/au/buy/jw-computers-apple-remote-control-bluetooth-tv-press-buttons-mjfm3lla-514001/',
            'https://www.kogan.com/au/buy/mighty-ape-apple-thunderbolt-3-usb-c-to-thunderbolt-2-adaptor-26771929/',
            'https://www.kogan.com/au/buy/vchain-apple-tv-4k-2nd-generation-2021-64gb-mxh02-apl-mxh02/',
            'https://www.kogan.com/au/buy/jw-computers-apple-lightning-to-35mm-audio-cable-12m-black-mr2c2fea-495881/',
            'https://www.kogan.com/au/buy/vchain-apple-tv-4k-2nd-generation-2021-32gb-mxgy2-apl-mxgy2/',
            'https://www.kogan.com/au/buy/shoptheglobe-1m-white-apple-watch-magnetic-charging-cable-1m-61-280383431-au/',
            'https://www.kogan.com/au/buy/trinity-connect-apple-usb-superdrive-optical-disc-drive-silver-dvdrrw-md564zma/']


google_home_entertainment_link_list =['https://www.kogan.com/au/buy/mobile-world-google-chromecast-with-google-tv-ga01919-au-snow-ggl-ga01919au-snw/',
            'https://www.kogan.com/au/buy/mob-google-chromecast-3rd-gen-ga00439-charcoal-grey-au-stock-842776106254/',
            'https://www.kogan.com/au/buy/spz-google-home-smart-speaker-home-assistant-white-white-googlehomeassitantwhite/',
            'https://www.kogan.com/au/buy/itz-google-chromecast-with-google-tv-hd-snow-ga03131-au-homgog03131/',
            'https://www.kogan.com/au/buy/vchain-google-chromecast-3-3rd-generation-1080p60-hz-video-wirelessly-stream-charcoal-gle-cc3/',
            'https://www.kogan.com/au/buy/az-eshop-google-chromecast-with-google-tv-media-streamer-4k-uhd-60-hz-hdr10-dolby-vision-support-hdmi-3730642005000/',
            'https://www.kogan.com/au/buy/itz-google-chromecast-3-hdmi-charcoal-grey-tvngog77970/',
            'https://www.kogan.com/au/buy/buy-today-pay-later-google-chromecast-with-google-tv-btpl_n1888/']




            

            



    

    




