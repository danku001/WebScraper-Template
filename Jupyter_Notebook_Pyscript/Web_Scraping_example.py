#!/usr/bin/env python
# coding: utf-8

# # WebScraping Practice

# ### Import all required libraries

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


# #### Connecting to the link provided by Keith Galli
# #### this is the link
# <blockquote> https://keithgalli.github.io/web-scraping/webpage.html </blockquote>

# In[2]:


link = "https://keithgalli.github.io/web-scraping/webpage.html"


# In[3]:


#requests implements browser style ssl verification by default
try:
    r = requests.get(link)
    r.raise_for_status()
    
except requests.exceptions.HTTPError as err404:
    #will occur if the webpage doesn't exist
    raise SystemExit(err404)
except requests.exceptions.ConnectionError as errc:
    #will occur if there is an error connecting to a webpage
    raise SystemExit(errc)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)


# ### Convert response to beautiful soup object

# In[4]:


soup = bs(r.content, features = "html.parser")


# In[5]:



#collecting the body
body = soup.body


# #### Grab all of the social Links from the webpage
# 

# ###### Do this in 3 different ways

# In[6]:


social = body.find('ul', class_ = 'socials')
social = social.find_all('a')
social_links = [link.get('href') for link in social]
print(social_links)


# In[7]:


social2 = body.find_all('li', class_= re.compile('social'))

social_links2 = [link.a.get('href') for link in social2]
print(social_links2)


# In[8]:


social3 = body.select('li.social a')

social_links3 = [link.get('href') for link in social3]
print(social_links2)


# ### Scrape the table

# In[9]:


table = body.select('table.hockey-stats')[0]
print(table)


# In[10]:


col_names = table.find('thead').find_all('th')
col_names = [name.string for name in col_names]

print(col_names)


# In[11]:


table_rows = table.find('tbody').find_all('tr')


# In[12]:


#get_text() works for nested elements
#.string only returns first level
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

table_df = pd.DataFrame(l, columns = col_names)


# In[13]:


table_df.head()


# In[14]:


#removing the duplicated columns
table_df = table_df.loc[:,~table_df.columns.duplicated()]


# In[15]:


table_df


# In[ ]:




