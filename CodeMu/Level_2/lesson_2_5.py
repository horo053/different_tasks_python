#5.1. Дана некоторая строка, например, вот такая: '023m0df0dfg0'. Получите сет позиций всех нулей в этой в строке.
def setZero(str_zero):
    set_zero = set()
    index = 0
    count = 0
    if '0' in str_zero:
        while len(str_zero) > index:
            if str_zero[index] == '0':
                set_zero.add(index)
                count += 1
            index += 1
        print('Индексы всех нулей в строке:', set_zero)
    else:print('Нулей в строке нет')

str_zero_one,str_zero_two = '023m0df0dfg0','gdrg234r'
setZero(str_zero_one)
setZero(str_zero_two)


print()
#5.2. Дана некоторая строка:'abcdefg'. Удалите из этой строки каждый третий символ. В нашем случае должно получится следующее:'abdeg'
def delThreeSymbol(del_three):
    res = ''
    index = 0
    list_str = list(del_three)
    len_list_str = len(list_str)
    while len_list_str > index:
        if index % 3 != 2:
            res += list_str[index]
        index += 1
    print(res)

str_del = 'abcdefg'
delThreeSymbol(str_del)


print()
#5.3. Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]. Поделите сумму элементов, стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях.
def divChetIndexOnNechetIndex(div_list):
    chet = 0
    nechet = 0
    for index, item in enumerate(div_list):
        if index % 2 == 0: chet += item
        else: nechet += item
    print(chet / nechet)

div_list = [1, 2, 3, 4, 5, 6]
divChetIndexOnNechetIndex(div_list)


print()
#5.4. Дана дата в следующем формате:['2025', '12', '31'].Преобразуйте эту дату в следующий кортеж:('31', '12', '2025')
def listInTupleDate(list_date):
    print(tuple(list_date[::-1]))

list_date = ['2025', '12', '31']
listInTupleDate(list_date)