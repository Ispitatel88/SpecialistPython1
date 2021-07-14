# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)
sal = []
com = []
import os
path = os.path.join('files', 'salaries.txt') 
with open(path, 'r', encoding='UTF-8') as f:
    for _ in zip(range(1), f): pass
    for line in f:
        el = line.rstrip()
        new_list = el.split()
        com.append(new_list)
        
path_2 = os.path.join('files', 'highly_paid.txt')
with open(path_2, 'a', encoding='UTF-8') as f:
    for i in range(len(com)):
       if int(com[i][-1]) > 60000:
            el = f' {com[i][0]} {com[i][1][0]}.{com[i][2][0]}.\n'
            f.write(el)
