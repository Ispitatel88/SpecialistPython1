# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit ame bt con sectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
#amount = text.count(len())
a = text.split(sep=" ")
i =0
j = 0
while i < len(a):

    if len(a[i]) == 3:
        #print(a[i])
        j = j + 1
    i += 1
print(j)
