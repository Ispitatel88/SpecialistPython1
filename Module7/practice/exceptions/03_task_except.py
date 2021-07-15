
# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
while True:
    inp_str = input('Enter five numbers: ')
    l = []

    try:

        list_of_num = list(map(lambda x: int(x), inp_str.split()))
        if len(list_of_num) != 5:
            raise ValueError
        else:
            break
    except ValueError:
        print('U enter incorrect data! Try again!')
for item in list_of_num:
    if item > 0:
        l.append(item)
min(l)
print(min(l))
