# -*- coding: utf-8 -*-
"""
Created on Mon Apr 01 21:10:41 2019

@author: vsarlis
"""


#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from IPython.core.debugger import set_trace
from collections import Counter
from more_itertools import unique_everseen
#pip install selenium
get_ipython().system('pip install beautifulsoup4')


# In[4]:


url = 'https://stats.nba.com/leaders/?Season=2019-20&SeasonType=Regular%20Season'
from selenium import webdriver
browser = webdriver.PhantomJS('C:\\Users\\vsarlis\\phantomjs.exe')
browser.get(url)
html = browser.page_source


# In[24]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
print(soup.prettify())


# In[10]:


table_data= soup.findAll('div', {'class' : "nba-stat-table"})


# In[21]:


players = []
GPs = []
MINs =[]
PTS = []
FGM =[]
errors= []
for x in soup.findAll('tr', {'data-ng-repeat' : "(i, row) in page track by row.$hash"}):
    try:
        players.append(x.a.text)
        GPs.append(x.findAll('td')[2].text)
        MINs.append(x.findAll('td')[3].text.replace('\n',"").strip())
        PTS.append(x.findAll('td')[4].text.replace('\n',"").strip())
        FGM.append(x.findAll('td')[5].text.replace('\n',"").strip())
    except:
        errors.append(" ")
players = list(unique_everseen(players))


# In[23]:


import pandas as pd
df = pd.DataFrame({'Name':players,'GP':GPs,'MIN':MINs,'PTS':PTS}).to_csv('NBAScraping1.csv')


# In[22]:


soup.find_all('p',{'class':')

