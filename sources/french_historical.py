from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from mysql_database import mysql_database

from historical_event import historical_event
from harvester import harvester

import logging

class french_historical(harvester):
    def __init__(self):
        self.event_links = []
        self.event_list = []
        self.source = 'france-pittoresque'
        
    def get_event_links(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('headless')
        browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)
        browser.get('https://www.france-pittoresque.com/spip.php?rubrique12')

        links_event = browser.find_elements_by_xpath('//td[@class="titreliste"]//a')
        for link in links_event:
            self.event_links.append(link.get_attribute('href'))
        browser.quit()

    def harvest(self):
        logging.info('Making api call in french_historical...')
        self.get_event_links()
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('headless')
        browser = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

        logging.info('Parsing french_historical results...')
        for link in self.event_links:
            browser.get(link)

            titles = browser.find_elements_by_xpath('//div[@id="rub"]//tr//td//div[@class="titre"]')
            title = [titlex.text for titlex in titles] 
            
            date = title[0].split(" ")[5]
            stories = browser.find_elements_by_xpath('//tr[@valign="top"]//td//div//table//tbody//tr//td//div//p')
            story = [storyx.text for storyx in stories]
             
            current_event = historical_event(date, story[0].encode('utf-8'), self.source, title[0].encode('utf-8'), link)
            self.event_list.append(current_event)
            
        browser.quit()
