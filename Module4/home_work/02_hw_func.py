# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.
def distance(a, b):
    d = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    return d

def min_distance(a, b, c):

    AB = distance(a, b)
    BC = distance(b, c)
    AC = distance(a, c)

    # cut_list = [AB, BC, AC]
    # min1 = min(cut_list)
    # print(f'Самый короткий отрезок: ', min1)

    if AB <= BC:
        if AB <= AC:
            return "Самый короткий отрезок AB: ",round(AB, 2)
        else:
            return "Самый короткий отрезок AC:", round(AC, 2)

    elif AC <= BC:
        return "Самый короткий отрезок AC:",round(AC, 2)
    else:
        return "Самый короткий отрезок BC:",round(BC, 2)


a = 2, 4
b = 5, 7
c = 8, 3
print(min_distance(a,b,c))
