import csv

with open('scientist.txt', encoding='utf-8' ) as f:
    reader = csv.reader(f, delimiter='#')
    reader = list(reader)
    authors = {}
    print('Разработчиками Аллопуринола были такие люди')
    for name, prep, date, comp in reader:
        if prep == 'Аллопуринол':
            authors[date] = name
            print(f'{name}-{date}')
    a = sorted(authors)
    print(f'Оригинальный рецепт пренадлежит: {authors[a[0]]}')




