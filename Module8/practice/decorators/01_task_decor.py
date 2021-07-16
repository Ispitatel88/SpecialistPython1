# Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
# Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
# ********
# *Привет*
# ********
# ****
# *23*
# ****
# (кол-во звездочек зависит от длины возвращаемого значения)
# def hello(word):
#
#     return word
# print(hello('Hi it is me!'))
def dec(hello):
    def around(word):
        # print('*'*len(word) + '\n*')
        print ('*'*(len(word)+2))
        print('*' + hello(word) + '*')
        print('*' * (len(word) + 2))
        #print('*' * len(word) + '\n*')
    return around


@dec
def hello(word):
    return (word)

hello('Hello it is me!')
