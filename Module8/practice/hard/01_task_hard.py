# "Банкомат"
# В банкомате есть купюры 5000, 2000, 1000 и 500 рублей.
# Напишите функцию, которая будет рассчитывать количество купюр, которыми можно будет выдать
# запрошенную пользователем сумму и возвращать ее в виде словаря, ключами в котором будут номиналы банкнот,
# а значениями кол-во банкнот. Если пользователь запросил некорректную сумму,
# нужно вывести дружественное сообщение об ошибке.
# Результат работы программы - текстовый отчет о номиналах и количестве купюр.

five = 10
two = 15
one = 7
half = 24

nominals = [5000, 2000, 1000, 500]
list_of_amount = [five, two, one, half]
sum_of_money = int(input('Enter wishes sum: '))
def money(S):
    list_of_needed = []    
    if S % 500 == 0 and S <= 5000 * five + 2000 * two + 1000 * one + 500 * half:
        amount_5 = S // 5000 # 4
        list_of_needed.append(amount_5)
        amount_2 = (S - amount_5*5000) // 2000  # 4500 // 2000 = 2
        list_of_needed.append(amount_2)
        amount_1 = ((S - amount_5*5000) - amount_2*2000)//1000 #  1
        list_of_needed.append(amount_1)
        amount_half = (((S - amount_5*5000) - amount_2*2000) - amount_1*1000)//500
        list_of_needed.append(amount_half)
        d = dict(zip(nominals, list_of_needed))
        return (d)
    elif S % 500 != 0:
        print("Operation can't be done. The sum should be divisible by 500.")
    else:
        print('Sorry, enter less sum.')


d = money(sum_of_money)
def take_money(dict_mon):
    l = ''
    try:
        for key in d:

            if d[key] != 0:
                l = l + (f'{nominals[nominals.index(key)]} - {d[key]} купюр(а)\n')
        print('Сумма будет выдана купюрами следующих номиналов: ')
        return l
    except:
        return 'Please try again!'
print(take_money(d))
