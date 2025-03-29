# Importing Importent libraries... 
from urllib.parse import quote 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import time
import os 



class Main():
    def __init__(self,filteredNumber,message):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.filteredNumber = filteredNumber
        self.message = message


    def login(self):
        os.system('cls')
        print('''
              
                    Please Login your whatsApp once we open it in your browser. 

              ''')
        time.sleep(10)
        
        # WhatsApp link 
        link = 'https://web.whatsapp.com'

        # opening link in chrome
        self.driver.get(link)

        # wating for the user to login in whatsApp web
        temp = input('If done Press Enter to Continue...... ')

    def sendMessage(self):
        filteredNumber = self.filteredNumber
         
        for i in filteredNumber:
            message = self.message
            for j in message:
                message = quote(message) 
                # typing  message to the given phone number  by link
                link2 = f'https://web.whatsapp.com/send/?phone={filteredNumber}&text={message}'
                self.driver.get(link2)
                time.sleep(10)


                # sending message 
                action =  ActionChains(self.driver)
                action.send_keys(Keys.ENTER)
                action.perform()
                time.sleep(10)

        exit = input('Press Enter to exit.')





