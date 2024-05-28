#7.1. Дан символ. Узнайте, в каком регистре этот символ - в верхнем или нижнем.
def howReg(symbol):
    if symbol == symbol.upper(): print(f'Символ "{symbol}" в верхнем регистре')
    else: print(f'Символ "{symbol}" в нижнем регистре')

one_symbol,two_symbol = 'l','K'
howReg(one_symbol)
howReg(two_symbol)


print()
#7.2. Дано некоторое число, например, такое:123789. Удалите из этого числа все нечетные цифры. В нашем случае получится такой результат:28
def delNechetNum(num):
    list_num = list(str(num))
    list_end = []
    print(list_num)
    for i in list_num:
        int_i = int(i)
        if int_i % 2 == 0: list_end.append(i)
    print(int(''.join(list_end)))

num = 123789
delNechetNum(num)


print()
#7.3. Дан кортеж с датой:('2025', '12', '31'). Преобразуйте эту дату в следующий словарь:{'year' : '2025','month': '12','day'  : '31',}
def tupleInDict(tuple_date):
    list_tuple = list(tuple_date)
    list_data = ['year', 'month', 'day']
    print(dict(zip(list_data, list_tuple)))

tuple_date = ('2025', '12', '31')
tupleInDict(tuple_date)