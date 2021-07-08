# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)
list_of_tup = list(tup)
list_of_tup.sort()
print(list_of_tup)
print(list_of_tup[-1])
