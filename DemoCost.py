#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


rate = 0.18
cost = 100
cost = cost + cost * rate * (rate > 0.13)
print(cost) # 118.0


# In[2]:


rate = 0.11
cost = 100
cost = cost + cost * rate * (rate > 0.13)
print(cost) # 118.0


# In[6]:


'''Для диапазона условие:
    если параметр больше 5 и меньше или равен 30, то (a - 5) * 1.2
    если параметр больше 30, то (a - 30) * 1.5

a = 40 # тестовое значение
y = 0 # укажите требуемое выражение
print(y) # 15.0'''

a = 40
y = (a - 5) * 1.2 *(5 < a <= 30) or (a - 30) * 1.5 * (a > 30)
print(y)




# In[11]:


''' Задание 2
Реализовать смену флага без if'''
'''n = 11
flag = False
if n%2 == 0:
    flag = True

print(flag)'''

n = 10
flag = False
flag = True * (n%2==0)
print(bool(flag))


# In[ ]:




