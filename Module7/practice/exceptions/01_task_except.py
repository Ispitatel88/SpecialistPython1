while True:
    try:
        size_of_fig = input('Enter size (numberxnumber): ')
        list_num = size_of_fig.split('x')
        amount_of_kv = round(int(list_num[0])/int(list_num[1]))
        print(amount_of_kv)
    except ValueError:
        print('Неккоректно введены данные')
