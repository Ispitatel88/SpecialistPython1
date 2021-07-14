# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения
import os
path = os.path.join('files', 'info.txt')
list_of_number = []
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip()
        try:
            if int(line):
                list_of_number.append(int(line))
        except: None
print(sum(list_of_number))
