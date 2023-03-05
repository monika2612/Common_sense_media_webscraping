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


soup.select('.link')


# In[4]:


author=set()
for name in soup.select(".link.link--title"):
    author.add(name.text)


# In[5]:


author


# In[ ]:




