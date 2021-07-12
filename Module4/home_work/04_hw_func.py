# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def nod(a_0, b_0): # Наибольший общий делитель
    while a_0 != b_0:
        if a_0 > b_0:
            a_0 = a_0 - b_0
        else:
            b_0 = b_0 - a_0
    return  a_0


def dr(a, b):
    a_0 = a.split('/')
    b_0 = b.split('/')
    if b_0[1] == a_0[1]: # проверка равенства знаменателей
        common_ratio = int(b_0[1]) # общий знаменатель
        res1 = int(a_0[0]) + int(b_0[0])
    else:
        common_ratio = int(b_0[1]) * int(a_0[1]) # общий знаменатель
        res1 = int(a_0[0]) * int(b_0[1]) + int(b_0[0]) * int(a_0[1])

    first_part = abs(res1) // int(common_ratio) # целая часть
    second_part = abs(res1) % int(common_ratio) # дробная часть
    nod_sf = nod(second_part, int(common_ratio)) # наибольший общий делитель дробной части
    second_part = int(second_part/nod_sf)
    common_ratio = int(common_ratio/nod_sf)
    common_ratio = str(common_ratio)


    if first_part != 0:
        if res1 < 0:
            res = str(-first_part) + ' ' + str(second_part) + '/' + common_ratio
        else:
            res = str(first_part) + ' ' + str(second_part) + '/' + common_ratio
    else:
        if res1 < 0:
            res = str(-second_part) + '/' + common_ratio
        else:
            res = str(second_part) + '/' + common_ratio


    return res

print(dr('3/10', '-1/5'))


