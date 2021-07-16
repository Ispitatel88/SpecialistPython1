# Чтобы	поднять холодильник на n-й этаж H-этажного дома, Коля вызвал бригаду грузчиков.
# За подъем холодильника на один этаж требуется заплатить 200 рублей, за спуск на один этаж — 100 рублей.
# За подъем и спуск на лифте плата не взимается.
# Несмотря на то, что в Колином доме есть лифт, ему возможно все же придется заплатить грузчикам,
# поскольку лифт останавливается только на каждом K-м этаже, начиная с первого
# (то есть на этажах с номерами 1, K+1, 2K+1, 3K+1, …).
# Требуется вычислить, за какую минимальную сумму грузчики доставят холодильник с первого этажа на этаж Коли.

# Формат входных данных
# Даны три числа, H - высота дома, N - этаж Коли и k - через сколько этажей останавливается лифт.
# H (2≤H≤100), n (2≤n≤H) и K (2≤k≤H–1).
# Формат выходных данных
# Выведите одно целое число - минимальную стоимость подъема

# Примеры для самопроверки:
# Входные данные-1:
# 20
# 7
# 4
# Выходные данные-1:
# 200
# Входные данные-2:
# 20
# 7
# 2
# Выходные данные-2:
# 0
def money_del(floor, period):
    a = (floor - 1)%period
    
    amount_period = (floor - 1) // period
    
    before = (a)*200
    after = ((period * amount_period + 1) + period - floor)*100
    
    if before > after:
        return after
    else:
        return before

print(money_del(20, 7, 2))
