import csv
from haversine import haversine, Unit

def loc():
    zip = input('Enter a ZIP Code to lookup: ')
    n = 0
    for i in rows():
        if i[0] == zip:
            print('ZIP Code ', i[0], ' is in ', i[3], i[4], i[5],
                '\n coordinates: ', i[1], '"N', i[2], '"W')
            n+=1
    if n == 0:
        print('Invalid or unknown ZIP Code')

def zip_f():
    city = input('Enter a city name to lookup: ').title()
    state = input('Enter the state name to lookup: ').upper()
    n = 0
    zips = []
    for i in rows():
        if i[3] == city and i[4] == state:
            zips.append(i[0])
            n+=1
    if n == 0:
        print('No ZIP Code found for', city, state )
    else:
        print('The following ZIP Code(s) found for', city, state, ':',', '.join(map(str, zips)))

def dist():
    first_c = input('Enter the first ZIP Code ')
    second_c = input('Enter the second ZIP Code ')
    city_1 = ()
    city_2 = ()
    n1 = 0
    n2 = 0
    for i in rows():
        if i[0] == first_c:
            city_1 = (float(i[1]),float(i[2]))
            n1 += 1
    for j in row:
        if j[0] == second_c:
            city_2 = (float(j[1]), float(j[2]))
            n2 += 1

    if n1 == 0 or n2 == 0:
        print('The distance between', first_c, 'and', second_c, 'cannot be determined')
    else:
        d = haversine(city_1, city_2, unit='mi')
        print('The distance between', first_c, 'and', second_c, 'is', format(d, '.2f'), 'miles')

def rows():
    with open('zip_codes_states.csv', 'r') as fl:
        reader = csv.reader(fl)
        row = list(reader)
    return row

while True:
    c = input('Enter command: loc, zip, dist, end ')
    if c == 'end':
        print('Done')
        break
    elif c == 'loc':
        loc()
    elif c == 'zip':
        zip_f()
    elif c == 'dist':
        dist()
    else:
        print('Invalid command, ignoring')

