
import csv

filename = "orderdata_sample.csv"
with open(filename, 'r', encoding="utf-8") as fh:
    reader = csv.reader(fh)
    rows = list(reader)  

rows[0].append('Total')


with open('new_orderdata_sample.csv', 'w', encoding="utf-8", newline="") as nf:
    writer = csv.writer(nf, quoting=csv.QUOTE_ALL)
    writer.writerow(rows[0])
    for row in rows[1:]:
        row.append(f'{float(row[3]) * float(row[4]) + float(row[5]): .2f}')
        writer.writerow([row])


