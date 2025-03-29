# Importing Importent libraries... 
from urllib.parse import quote 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import time
import os 

# Clear Screen
os.system("cls")

# User Banner ; 








numbers = []
with open('./db/numbers.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rsplit())


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link = 'https://web.whatsapp.com'

# opening link in chrome
driver.get(link)

# wating for the user to login in whatsApp web
time.sleep(15)

for num in numbers:

    msg = f'Hello sir, This is your {num}'
    msf = quote(msg)
    # typing  message to the given phone number  by link
    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
    driver.get(link2)
    time.sleep(10)

    # sending message 
    action =  ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(10)


# Stoping chrome from closing and terminate the program
time.sleep(2000)