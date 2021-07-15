# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random

new_list = []
for i in range(random.randrange(1, 1000)):
    i = random.randrange(-100, 100)
    new_list.append(i)
print(new_list)

amount = (list(filter(lambda x: x<=10, new_list)))
print(amount)
print(len(amount))

amount_positive = (list(filter(lambda x: x>0, new_list)))
print(sum(amount_positive))

amount_2 = (list(filter(lambda x: x%2==0 and x != 0, new_list)))
avr = sum(amount_2)/len(amount_2)
