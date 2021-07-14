# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла
import os
def log(text, file="log.txt"):
    path = file
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(text)


log('I have done it.\n')
log('message', file='log01.txt')
