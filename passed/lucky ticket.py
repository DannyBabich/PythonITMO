#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[3]:


ticket = list(input('Введите номер билета '))
if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[3])+int(ticket[4])+int(ticket[5]):
    print('Билет счастливый')
else:
    print('Билет не счастливый')
    

