#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[3]:


'''Создайте три списка, каждый из которых должен содержать десять значений.
Первый – названия продуктов, второй – стоимость продукта, а третий – трехзначный
код сотрудника, оформившего продажу.
Требуется объединить все три списка в один список.
Рекомендация: используйте встроенную функцию Python zip(), изучите порядок
ее работы согласно официальной документации.'''

a = ['молоко', 'мед', 'хлеб', 'вода', 'кофе', 'чай', 'сахар', 'сироп', 'печенье', 'молоток']
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [123, 234, 345, 456, 567, 678, 789, 890, 901, 321]
abc = []
for item in zip(a,b,c):
    abc.append(item)
print(abc)


# In[ ]:



