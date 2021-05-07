#!/usr/bin/env python
# coding: utf-8

# In[39]:


Book1=open("Book1.txt",encoding='utf-8')
Book1List= Book1.read().split(' ')


# In[40]:


Book2=open("Book2.txt",encoding='utf-8')
Book2List= Book2.read().split(' ')


# In[41]:


print(set(Book1List)&set(Book2List))

