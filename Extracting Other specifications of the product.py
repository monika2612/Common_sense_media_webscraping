#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
from bs4 import BeautifulSoup as bs
import requests


# In[2]:


url = 'https://www.commonsensemedia.org/lists/50-books-all-kids-should-read-before-theyre-12'

source = requests.get(url)
data = source.content
soup = bs(data, "lxml")


# In[3]:


#get other details and specifications of the product
specification=soup.find('p',class_="review-one-liner")
print(specification)
specification.text


# In[ ]:




