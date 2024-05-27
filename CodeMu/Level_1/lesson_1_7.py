#7.1. Дан словарь: {'a': 1,'b': 2,'c': 3,'d': 4,}. Найдите сумму элементов этого словаря.
def sumDictValue(value):
    l = 0
    listD = list(value.values())
    for n in listD:
        l += n
    print(l)

dictVal = {'a': 1,'b': 2,'c': 3,'d': 4,}
sumDictValue(dictVal)


print()
#7.2. Дан словарь:{'a': 1,'b': 2,'c': 3,'d': 4,}. Найдите сумму квадратов элементов этого словаря.
def sumDictValueQtr(valueQtr):
    l = 0
    listD = list(valueQtr.values())
    for n in listD:
        l += n**2
    print(l)

sumDictValueQtr(dictVal)


print()
#7.3. Дана строка:'abcde'. Получите список букв этой строки..
def listLatter(latter):
    print(list(latter))

strLatter = 'abcde'
listLatter(strLatter)


print()
#7.4. Дано некоторое число:12345. Получите список цифр этого числа.
def listInt(intList):
    print(list(str(intList)))

intNum = 12345
listInt(intNum)


print()
#7.5. Дано некоторое число:12345. Переверните его:
def recersInt(intRevers):
    strInt = str(intRevers)
    revStr = strInt[::-1]
    revInt = int(revStr)
    print(revInt)

recersInt(intNum)


print()
#7.6. Дано некоторое число:12345. Найдите сумму цифр этого числа.
def sumNum(intNum):
    k = 0
    while intNum > 0:
        k += intNum%10
        intNum = intNum//10
    print(k)

sumNum(intNum)