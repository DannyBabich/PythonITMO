import names
lst = [names.get_first_name() for i in range(0,100)]
lst1 = []
lst2 = []

for i in lst:
    if i[0] == 'A' or i[0] == 'M':
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1,'\n',lst2)








