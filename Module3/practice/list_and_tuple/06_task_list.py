# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input('a1 = '))     # Первое число
second_number = int(input('a2 = '))    # Второе число

l_3 = []
for i in range(first_number, second_number):
    if i%3 == 0:
        l_3.append(i)
print(l_3)
