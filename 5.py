import csv
import random


def create_hash(name):
    a = [i for i in range(1024)]
    random.shuffle(a)
    name = name.replace(' ', '')
    s = 0
    for i in name:
        code = ord(i) % 1024
        s += a[code]
    return s % 2028


with open('scientist.txt', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter='#'))
    reader[0].append('Hash')
    for i in range(1, len(reader)):
        hash = create_hash(reader[i][0])
        reader[i].append(hash)

with open('cientist_with_hash.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='#')
    writer.writerow(reader[0])
    writer.writerows(i for i in reader[1:])
