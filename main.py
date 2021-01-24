#!/bin/env python3
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent
import colorama
from colorama import Fore, Style
views = 0
class Main():
    def __init__(self):
        self.author = '__th3end0f3v4ng3l10n__'

    def log(self,text):
        print('[ ',Fore.GREEN + '+','] ', Style.RESET_ALL, '{}'.format(text))
    def function(self):
        options = Options()

        ua = UserAgent()
        ua.random
        #print(ua)
        options.add_argument(f'user-agent={UserAgent}')
        options.add_argument('--headless')

        self.driver = webdriver.Chrome(options = options)
        self.driver.get('https://www.youtube.com/watch?v=Ge9Tr9T17XE&feature=youtu.be')
        button = self.driver.find_element_by_class_name('ytp-large-play-button')
        button.click()
        sleep(15)
        self.driver.close()

root = Main()
while views < 1000:

    try:
        for i in range(1,6):
            root.function()
            root.log(str(views))
            views +=1
    except:
        views -= 1
    if views > 43:
        sleep(3000)
