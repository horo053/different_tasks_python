#7.1. Дан словарь: {'a': 1,'b': 2,'c': 3,'d': 4,}. Найдите сумму элементов этого словаря.
def sumDictValue(value):
    l = 0
    list_d = list(value.values())
    for n in list_d:
        l += n
    print(l)

dict_val = {'a': 1, 'b': 2, 'c': 3, 'd': 4, }
sumDictValue(dict_val)


print()
#7.2. Дан словарь:{'a': 1,'b': 2,'c': 3,'d': 4,}. Найдите сумму квадратов элементов этого словаря.
def sumDictValueQtr(value_qtr):
    l = 0
    list_d = list(value_qtr.values())
    for n in list_d:
        l += n**2
    print(l)

sumDictValueQtr(dict_val)


print()
#7.3. Дана строка:'abcde'. Получите список букв этой строки..
def listLatter(latter):
    print(list(latter))

str_latter = 'abcde'
listLatter(str_latter)


print()
#7.4. Дано некоторое число:12345. Получите список цифр этого числа.
def listInt(int_list):
    print(list(str(int_list)))

int_num = 12345
listInt(int_num)


print()
#7.5. Дано некоторое число:12345. Переверните его:
def recersInt(int_revers):
    str_int = str(int_revers)
    rev_str = str_int[::-1]
    rev_int = int(rev_str)
    print(rev_int)

recersInt(int_num)


print()
#7.6. Дано некоторое число:12345. Найдите сумму цифр этого числа.
def sumNum(int_num):
    k = 0
    while int_num > 0:
        k += int_num % 10
        int_num = int_num // 10
    print(k)

sumNum(int_num)