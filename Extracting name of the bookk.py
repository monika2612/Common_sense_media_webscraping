#!/usr/bin/env python
# coding: utf-8

# In[2]:


import bs4
from bs4 import BeautifulSoup as bs
import requests


# In[ ]:





# In[3]:


url = 'https://www.commonsensemedia.org/lists/50-books-all-kids-should-read-before-theyre-12'

source = requests.get(url)
data = source.content
soup = bs(data, "lxml")


# In[3]:





# In[4]:


soup.select('.link.link--title')


# In[5]:


bname=set()
for name in soup.select(".link.link--title"):
    bname.add(name.text)
    


# In[6]:


bname


# In[ ]:




