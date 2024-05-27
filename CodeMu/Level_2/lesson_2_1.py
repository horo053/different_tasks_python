#1.1. Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
def httpStr(httpS):
    need_items = [item for item in httpS if item.startswith('http://')]
    print(need_items)

listStrHttp = ['http://abcdef','vdxjkvkd','kuhfgj','http://grg']
httpStr(listStrHttp)


print()
#1.2. Дана некоторая строка. Найдите позицию первого нуля в строке.
def nulInStr(indexNull):
    if indexNull.find('0') == -1: print('Нули в строке отсутствуют')
    else: print(indexNull.find('0'))

strNull,strNotNull = 'rg523dr0jy3fg','rg34regreg3534'
nulInStr(strNull)
nulInStr(strNotNull)


print()
#1.3. Дан список. Удалите из него элементы с заданным значением.
def delElementList(listElem):
    for n in listElem:
        if n == 'a': listElem.remove('a')
    print(listElem)

listElem = ['a', 'r', 4, 'h', 'a', 98, 'u', 'f', 12, 'c', 'a']
delElementList(listElem)


print()
#1.4. Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти.
def numFive(x,y):
    listFive = []
    for n in range(x, y):
        if int(str(n)[0:1]) + int(str(n)[1:2]) == 5: listFive.append(n)
    print(listFive)

x,y = 10,1000
numFive(x,y)


print()
#1.5. Дана некоторая строка:'abcdeabc'. Очистите ее от дублей символов:'abcde'
def strNotDuble(strSet):
    print(''.join(sorted(list(set(strSet)))))

strSet = 'abcdeabc'
strNotDuble(strSet)