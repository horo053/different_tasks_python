#4.1. Дана некоторая строка с буквами и цифрами. Получите позицию первой цифры в этой строке.
def oneIntInStr(str_one_int):
    if (any(character.isdigit() for character in str_one_int)):
        str = (character.isdigit() for character in str_one_int)
        list_str = list(str)
        print('индекс:', list_str.index(True), 'число:', str_one_int[list_str.index(True)])
    else:print('В строке нет чисел')

str_one_int,str_nan_int = 'rdffs47rgdkrmgd3gd', 'rgrdfgrd'
oneIntInStr(str_one_int)
oneIntInStr(str_nan_int)


print()
#4.2. Дано число. Выведите в консоль количество четных цифр в этом числе.
def chetInInt(int_chet):
    count = 0
    while int_chet > 0:
        if (int_chet % 10) % 2 == 0: count += 1
        int_chet = int_chet // 10
    print('Четное количество цифр в числе:', count)

int_chet,int_ne_chet = 65378412, 13597
chetInInt(int_chet)
chetInInt(int_ne_chet)


print()
#4.3. Дан словарь: { 'a': 1, 'b': 2, 'c': 3, 'd': 4, }. Получите список его ключей ['a', 'b', 'c', 'd']
def keyInDict(dict_for_key):
    print(list(dict_for_key.keys()))

dict_for_key = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
keyInDict(dict_for_key)


print()
#4.4. Дана некоторая строка: 'abcde'. Переведите в верхний регистр все нечетные буквы этой строки. В нашем случае должно получится следующее: 'AbCdE'
def upperNechetInStr(str_up_chet):
    res = ''
    for i, s in enumerate(str_up_chet):
        if i % 2 != 0: res += s.upper()
        else: res += s
    print(res)

str_up_chet = 'abcde'
upperNechetInStr(str_up_chet)


print()
#4.4. Дана некоторая строка со словами: 'aaa bbb ccc'. Сделайте заглавным первый символ каждого слова в этой строке. В нашем случае должно получится следующее: 'Aaa Bbb Ccc'
def upperOneSymbolInStr(str_up_one):
    print(str_up_one.title())

str_up_one = 'aaa bbb ccc'
upperOneSymbolInStr(str_up_one)


print()
#4.4. Дана дата в следующем формате: '2025-12-31' Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')
def dateInTuple(date_in_tuple):
    listDate = date_in_tuple.split('-')
    print(tuple(listDate)[::-1])

date_in_tuple = '2025-12-31'
dateInTuple(date_in_tuple)