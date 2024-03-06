import csv


def binary_search(a, el, needToFind):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        midValue = a[mid][el]
        if midValue == needToFind:
            return mid
        if midValue > needToFind:
            high = mid - 1
        else:
            low = mid + 1
    return True


with open('scientist.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='#')
    data = list(reader)[1:]

    time = input()
    while time != 'эксперимент':
        time = time.replace('.', '-')
        el = binary_search(data, 2, time)
        time = data[el][2]
        prep = data[el][1]
        name = data[el][0].split()
        name = f'{name[0]} {name[1][0]}.{name[2][0]}'
        print(f'Учёный {name} создал препарат: {prep}-{time}')
        time = input()
