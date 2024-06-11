#1
import os
folder = r'/Users/denisbabich/Desktop/ITMO/python/Prictice_4 '
answ = set()
search = input()

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r') as fp:
        for line in fp:
            if search in line:
                answ.add(filename)
for i in answ:
    print(i)

#2
import csv

file = 'file.txt'

with open(file, 'r+') as fh:
    content = csv.reader(fh)
    lines = list(content)

letters = 0
words = 0
for line in lines:
    for i in line:
        for j in i:
            if j != ' ' and j != '\n' and j != '.':
                letters += 1
            else:
                continue
    words += len(line[0].split())


print('Input file contains:''\n', letters, 'letters' '\n', words, 'words' '\n', len(lines), 'lines')


#3
from pathlib import Path

home = Path.home()
my_folder = home / "practice4f"
if not my_folder.exists():
    my_folder.mkdir()
file1 = my_folder / "file1.txt"
file1.touch()
(my_folder / "file2.txt").touch()
my_folder.joinpath("image.png").touch()
(my_folder / "images").mkdir(exist_ok=True)
for f in my_folder.glob('*.png'):
    path_destination = Path(my_folder /"images") / f.name
    f.replace(path_destination)

#4
from pathlib import Path
home = Path.home()
(home / "file1.txt").touch()
(home / "file2.txt").touch()
(home / "file3.txt").touch()
catalog = input('Введите имя каталога ')
new_folder = home / catalog
if not new_folder.exists():
    new_folder.mkdir()
for f in home.glob('*.txt'):
    path_destination = Path(home / catalog) / f.name
    f.replace(path_destination)