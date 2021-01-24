#!/bin/env python3
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent
views = 0
class Main():
    def __init__(self):
        self.author = '__th3end0f3v4ng3l10n__'


    def function(self):
        options = Options()

        ua = UserAgent()
        ua.random
        print(UserAgent)
        options.add_argument(f'user-agent={UserAgent}')

        self.driver = webdriver.Chrome(options = options)
        self.driver.get('https://www.youtube.com/watch?v=Ge9Tr9T17XE&feature=youtu.be')
        button = self.driver.find_element_by_class_name('ytp-large-play-button')
        button.click()
        sleep(15)
        self.driver.close()

root = Main()
while views < 10:
    views += 1
    root.function()
