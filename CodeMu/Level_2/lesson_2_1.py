#1.1. Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
def httpStr(http_s):
    need_items = [item for item in http_s if item.startswith('http://')]
    print(need_items)

list_str_http = ['http://abcdef', 'vdxjkvkd', 'kuhfgj', 'http://grg']
httpStr(list_str_http)


print()
#1.2. Дана некоторая строка. Найдите позицию первого нуля в строке.
def nulInStr(index_null):
    if index_null.find('0') == -1: print('Нули в строке отсутствуют')
    else: print(index_null.find('0'))

str_null,str_not_null = 'rg523dr0jy3fg', 'rg34regreg3534'
nulInStr(str_null)
nulInStr(str_not_null)


print()
#1.3. Дан список. Удалите из него элементы с заданным значением.
def delElementList(list_elem):
    for n in list_elem:
        if n == 'a': list_elem.remove('a')
    print(list_elem)

list_elem = ['a', 'r', 4, 'h', 'a', 98, 'u', 'f', 12, 'c', 'a']
delElementList(list_elem)


print()
#1.4. Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.
def numFive(x,y):
    list_five = []
    for n in range(x, y):
        if int(str(n)[0:1]) + int(str(n)[1:2]) == 5: list_five.append(n)
    print(list_five)

x,y = 10,1000
numFive(x,y)


print()
#1.5. Дана некоторая строка:'abcdeabc'. Очистите ее от дублей символов:'abcde'
def strNotDuble(str_set):
    print(''.join(sorted(list(set(str_set)))))

str_set = 'abcdeabc'
strNotDuble(str_set)