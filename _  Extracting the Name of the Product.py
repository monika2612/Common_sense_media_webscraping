#!/usr/bin/env python
# coding: utf-8

# In[34]:


import bs4
from bs4 import BeautifulSoup as bs
import requests


# In[35]:


url = 'https://www.commonsensemedia.org/lists/50-books-all-kids-should-read-before-theyre-12'

source = requests.get(url)
data = source.content
soup = bs(data, "lxml")


# In[39]:


name=soup.find('h3',class_="review-title")
print(name)


# In[40]:


name.text


# In[ ]:




