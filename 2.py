import csv


def QuickSort(a, el):
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i][el] > a[i + 1][el]:
                a[i][el], a[i + 1][el] = a[i + 1][el], a[i][el]
        n += 1
    return a


with open("scientist.txt", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='#')
    data = list(reader)[1:]
    new_data = QuickSort(data, 2)
    print(new_data)
with open('scientist.txt', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='#')
    writer.writerow(['ScientistName', 'preparation', 'date', 'components'])
    writer.writerows(i for i in new_data)
