#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[13]:


string1 = "This is a string."
string2 = " This is another string."
print(string1 + string2)
print(len(string2))
print(string2.upper())
print(string1.lower())
print((string1 + string2).title())
print(('0' + string1 * 2 + '0').strip('0'))


# In[15]:


d = 'qwertyuiop'
ch = d[-2]
print(ch)


# In[17]:


d = 'qwertyuiop'
ch = d[:-1:2]
print(ch)
d[5] = 'j'
print(d) #'str' object does not support item assignment


# In[28]:


a = 25
b = 5
print(a/b, b//a, b**a, b%a)


# In[32]:


'''param = 'string' + 15
print(param) can only concatenate str (not "int") to str'''
param = 'string' + str(15)
print(param)


# In[1]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)


# In[2]:


a = 1/3
print("{:7.3f}".format(a)) #3f колличество знаков после запятой
print(len("{:7.3f}".format(a))) # ':7' колличество знаков для вывода


# In[36]:


a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


# In[3]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:6.3e}".format(n3))
print(n1 + " plus " + n2 + " = ", "{:10.4f}".format(n3))


# In[12]:


list1 = [82,8,23,97,92,44,17,39,11,12]
print(dir(list), end = ',')
help(list.insert)
help(list.append)
help(list.remove)


# In[32]:


list1 = [82,8,23,97,92,44,17,39,11,12]
list1[8] = 'string'
print(list1)
list1.append('string2')
print(list1)
list1.insert(2,'string3')
print(list1)
list1.remove('string3')
print(list1)
list1.pop()
print(list1)


# In[35]:


list1 = [82,8,23,97,92,44,17,39,11,12]
list1.sort(reverse = True)
print(list1)
list1.sort(reverse = False)
print(list1)


# In[37]:


list22 = [3,5,6,2,33,6,11]
list33 = sorted(list22,reverse = True)
print(list33)


# In[40]:


print(dir(tuple), end = ',')


# In[43]:


help(tuple.count)
help(tuple.index)


# In[50]:


seq = (2,8,23,97,92,44,17,39,11,12,11)
print(seq.count(11)) #возвращает колличество вхождения
print(seq.index(44)) #возвращает индекс первого вхождения
listseq = list(seq)
print(type(listseq))


# In[60]:


D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
D['food'] = 'Pineapple'
D['quantity'] += 400
print(D)
d = {}
print(len(d))


# In[71]:


print(dir(dict), end=',')
help(dict.update)


# In[73]:


data = {}
name  = str(input('Enter your Name '))
age  = str(input('Enter your Age '))
data[name] = age
print(data)


# In[93]:


rec = {}
firstname = 'Denis' #str(input('Enter your Name '))
lastname = 'Babich' #str(input('Enter your Lastname '))
age  = 38 #int(input('Enter your Age '))
job = 'Banker' #str(input('Enter your Profession '))
name_l = {}
name_l['firstname'] = firstname
name_l['lastname'] = lastname
joblist = []
joblist.append(job)
rec['name'] = name_l
rec['job'] = joblist
rec['job'].append('janitor')
rec['age'] = age
print(rec)
print(rec['name']['firstname'],rec['name']['lastname'])
#print(rec['name']['firstname'],rec['name']['lastname'],' age ', str(rec['age']), 'Profession', rec['job'])



# In[ ]:
