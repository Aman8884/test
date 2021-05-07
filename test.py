import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import re
import pandas as pd
from bs4 import BeautifulSoup

class retreive_data:
  def __init__(self):
    self.url=[]
  def scrape_data(self):
      url = 'https://www.iqsdirectory.com/data-loggers/data-loggers-2/'### url of base website
      reqs = requests.get(url)
      soup = BeautifulSoup(reqs.text, 'html.parser')
      content = soup.find_all(class_ = {'cname'})
      prices = soup.find_all(itemprop='name')
      urls = []
      company_names=[]
      contact=[]
      url=[]
      addr=[]
      z=soup.find_all('a')
      ### create data frame
      df = pd.DataFrame(columns = ['Name', 'Address', 'Contact', 'URL', 'Revenue','Number of employees','Founded'])
      for link in content:
          cells      = link.find_all(itemprop='name')
          company_names.append(cells[0].get_text())
          method=link.find(class_ = 'addr').get_text()
          con=re.split('\n',method)[2]
          contact.append(re.split('\n',method)[2])
          ad=re.split('\n',method)[1]
          addr.append(re.split('\n',method)[1])
          event_url  = link.find('a').get('href')
          url.append(event_url)
          df = df.append({'Name' : cells[0].get_text(), 'Address' : ad, 'Contact':con, 'URL':event_url, 'Revenue':0,'Number of employees':0, 'Founded':0},
                ignore_index = True)

      return df
d=retreive_data()
final_data=d.scrape_data()

print('Hello World')
print('Hello')
