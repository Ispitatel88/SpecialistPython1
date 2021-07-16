# Напишите функцию декоратор, которая округляет значение декорируемой функции до двух знаков после  запятой.
# Если округление невозможно, например там строка, или не требуется(целое число) то оставляем результат без изменений.
# Примечание: используйте встроенную функцию round()
def deco(our_number):
    def wrapper(num):
        if type(num) is not float:
            return our_number(num)
        else:
            res = our_number(num)
            return round(res, 2)
    return wrapper



@deco
def our_number(num):
    return num

our_num = 'hguyg'
print(our_number(our_num))
