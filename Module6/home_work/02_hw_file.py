# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения
import os
path = os.path.join('files', 'info.txt')

# !!! ВАРИАНТ № 1 C TRY

# list_of_number = []
# with open(path, 'r', encoding='UTF-8') as f:
#     for line in f:
#         line = line.rstrip()
#         try:
#             if int(line):
#                 list_of_number.append(int(line))
#         except: None
# print(sum(list_of_number))

# !!! ВАРИАНТ № 2 БЕЗ TRY

new = []
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip()
        new.append(line)
sum_of_num = 0
new_list_of_num = []
for item in new:
    if item.isdigit() or (item[0] == '-' and item[1:].isdigit()):
        num = int(item)
        new_list_of_num.append(num)

print(sum(new_list_of_num))
