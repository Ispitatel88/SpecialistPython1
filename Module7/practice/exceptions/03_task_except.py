
# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.

# ВТОРОЙ ВАРИАНТ


while True:
    inp_str = input('Enter five numbers: ')
    try:
        l = inp_str.split()
        if len(l) != 5:
            raise ValueError
        else:
            min_2 = min(list(filter(lambda x:int(x)>0, l)))
            break
    except ValueError:
        print('U enter incorrect data! Try again!')
print(min_2)
