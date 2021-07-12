# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Вариант № 1

def lucky_ticket(number):
    num = 0
    copy_number = number

    while number > 0:
        new_number = number%10
        num = num*10 + new_number
        number = number//10

    print(num)

    if num == copy_number:
        return num and True
    else:
        return num and False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Вариант № 2

def lucky_ticket_str(number):
    number_str = str(number)
    new_number = number_str[::-1]
    if new_number == number_str:
        return number, True # return tuple
    else:
        return number, False

print(lucky_ticket_str(5555))
