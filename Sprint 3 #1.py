#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

chars = 'abcdefghijklmnopgrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
        print(password)


# In[ ]:




