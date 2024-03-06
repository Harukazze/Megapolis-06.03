import csv
import random

strings = 'qwertyuiopasdfghjklzxcvbnm'
integers = list('01234567890')


def create_login(name):
    name = name.split()
    print(name)
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


def create_password():
    password = random.choices(strings, k=10) + integers
    random.shuffle(password)
    return ''.join(password)


with open('scientist.txt', encoding='utf-8') as f:
    reader = list(csv.reader(f, delimiter='#'))
    reader[0].append('Login')
    reader[0].append('Password')
    for i in range(1, len(reader)):
        name = reader[i][0]
        login = create_login(name)
        password = create_password()
        reader[i].append(login)
        reader[i].append(password)
        print(reader[1])

with open('scientist_password.csv', 'w', encoding='utf-8', newline='') as f:
    print(reader)
    writer = csv.writer(f, delimiter='#')
    writer.writerow(reader[0])
    writer.writerows(i for i in reader[1:])
