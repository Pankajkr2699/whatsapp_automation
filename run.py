# Importing codes to the main file 
from urllib.parse import quote 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import os 
import time 
from colored import fg 

# code import 
from banner.banner import Banner 
from lib.filter import Data  
# from lib.main import Main


# UI Message 
print(f'''
            {fg("red")}Sorry for interrupting. \n 
            Please run it on full screen for a 
            better experience.
''')

time.sleep(5)


# Banner section 
os.system('cls')
banner = Banner()
banner.banner1()

# Loading Animation 
banner.loadingAnimation()

# Menu Designing 


#Getting Phone Number  
banner.banner1()
data = Data()
filteredNumber = data.number()

print(filteredNumber)
print(type(filteredNumber))


# Message
message = data.message()
print(message)
print(type(message))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Clear Screen
os.system("cls")

print('''
     Please Login your whatsApp once we open it in your browser. 
''')
time.sleep(10)

# WhatsApp link 
link = 'https://web.whatsapp.com'

# opening link in chrome
driver.get(link)

# wating for the user to login in whatsApp web

time.sleep(20)



for i in filteredNumber:
    for j in message:
        text = quote(j) 
        # typing  message to the given phone number  by link
        link2 = f'https://web.whatsapp.com/send/?phone={i}&text={text}'
        driver.get(link2)
        time.sleep(15)


        # sending message 
        action =  ActionChains(driver)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(2)

exit = input('Press Enter to exit.')