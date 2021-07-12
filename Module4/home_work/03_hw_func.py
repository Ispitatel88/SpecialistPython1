# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def circle_inside(r1, r2, xy1, xy2 ):
    """
    Проверяет входит ли одна окружность в другую
    :param r1: Радиус первого круга
    :type r1: int
    :param r2: Радиус вторго круга
    :type r2: int
    :param xy1: координаты центра первого круга
    :type xy1: tuple
    :param xy2: координаты центра второго круга
    :type xy2: tuple
    :return:
    """
    if (r1 - r2) ** 2 >= (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2:
        if r1 > r2:
            return "the second circle is inside the first circle"
        else:
            return "the first circle is inside the second circle"
    else:
        return "the circle isn't inside the another circle"



r1 = 7
r2 = 3
a = (0,0)
b = (10,10)

print(circle_inside(r1, r2, a, b))
