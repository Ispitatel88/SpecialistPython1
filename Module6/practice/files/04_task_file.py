# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
list_of_names_fr = []
import os
import collections
path = os.path.join('files', 'fruits.txt')
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        el = line.rstrip()
        if line != '\n':
            list_of_names_fr.append(line)
list_of_names_fr.sort()
list_char = []
for i in range(len(list_of_names_fr)):
    list_char.append(list_of_names_fr[i][0])
    dict_char = dict(collections.Counter(list_char))

for key in dict_char:
    for item in range(len(list_of_names_fr)):
        if key == list_of_names_fr[item][0]:
            with open(os.path.join('files', f'{key}_fruits.txt'), 'a', encoding='UTF-8') as newfr:
                newfr.write(list_of_names_fr[item])
