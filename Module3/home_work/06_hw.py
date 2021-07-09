# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3800
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
#1
brands = []
print("Товары на складе представлены брэндами: ")
for i, item in enumerate(items, 1):
    print(f'{i}. {item["brand"]}',end=", ")
    brands += [item['brand']]
print('\n')

#2
#Вариант 1
print("На складе больше всего товаров брэнда(ов): ")
from collections import Counter
brand_dict = dict(Counter(brands))

max(brand_dict.values())
new_dict = {}
for key, value in brand_dict.items():
    if value == max(brand_dict.values()):

        new_dict.update({key:value})
print(new_dict)

#Вариант 2
print("На складе больше всего товаров брэнда(ов): ")
puma_amount = 0
adidas_amount = 0
reebok_amount = 0
for item in items:
        if item['brand'] == 'puma':
        puma_amount += 1
    elif item['brand'] == 'adidas':
        adidas_amount += 1
    elif item['brand'] == 'reebok':
        reebok_amount += 1
print('reebok_amount: ', reebok_amount)
print('puma_amount: ', puma_amount)
print('adidas_amount: ', adidas_amount)

#3
print("На складе самый дорогой товар брэнда(ов): ")

max_price = {}
for i in  items:
    if i['price'] > items[0]['price']:
        max_price.update({i['brand']:i['price']})
list_brands = []
for key in max_price:
    list_brands.append(key)
print(*list_brands, sep=', ')
