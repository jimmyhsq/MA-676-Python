#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 1 a)
a = list(range(1,21))
print(a)


# In[12]:


# b) 
b = list(reversed(range(1,21)))
print(b)


# In[16]:


# c)
c = list(range(1,21))+list(reversed(range(1,21)))
print(c)


# In[17]:


# d)

d = [4,6,3]
print(d * 10)


# In[23]:


# e) 

e = [4,6,3]*10 + [4]  

print(e)


# In[35]:


# 2 
import numpy as np
f = np.arange(3, 6.1, 0.1)
x = [np.exp(i) * np.cos(i) for i in f]
print(x)


# In[36]:


# 3

g = list(range(1,26))
x = [2**i/i for i in g]
print(x)
    


# In[38]:


# 4 a)
a = list(range(1,21))
x = [a[i-1]-a[20-i] for i in a]
print(x)


# In[41]:


# 4 b) 
a = list(range(1,21))
x =[a[i-1] % 2 == 0 for i in a]
print(x)


# In[24]:


# 5 a) 
import re 
letetrs = []
with open('lorem.txt','r') as letter: 
    count = 0 
    text = letter.read()
    text_1 = re.findall(r"[\w]+", text)
    for character in text_1:
        if (len(character) != 1) & (len(character) != 4) & (len(character) != 7):
            count += 1 
            letters.append(character)
print(count)
        


# In[13]:


# 5 b)

letters = []
with open('lorem.txt') as letter:
    count = 0
    text = letter.read()
    for character in text:
        if character.isupper():
            count += 1
            letters.append(character)
print(count)

