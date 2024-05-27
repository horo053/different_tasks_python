#2.1. Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
def countNegativeNumber(countNeg):
    countNum=0
    for n in countNeg:
        if n < 0: countNum += 1
    print(countNum)

listInt = [-1,4,35,-654,-446]
countNegativeNumber(listInt)


print()
#2.2. Дан список с числами. Оставьте в нем только положительные числа.
def listPositiveNum(listPositive):
    need_items = [item for item in listPositive if item < 0]
    print(need_items)

listPositiveNum(listInt)


print()
#2.3. Дана строка. Удалите предпоследний символ из этой строки.
def delStrSymbol(delStr):
    listStr = list(delStr)
    listStr.pop(-1)
    print(''.join(listStr))

delStr = 'asdfgh'
delStrSymbol(delStr)


print()
#2.4. Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.
def htmlStr(htmlS):
    listWithHtml = [el for el in htmlS if el.endswith('.html')]
    print(listWithHtml)

listStrHtml = ['fdgdgr.html','dfgg.grhr','xcvbvcn.html','tfhtffh']
htmlStr(listStrHtml)


print()
#2.5. Дан список с дробями: [1.456, 2.125, 3.32, 4.1, 5.34]
def roundFloat(listFloat):
    l = 0
    while l < len(listFloat):
        listFloat[l] = round(listFloat[l],1)
        l += 1
    print(listFloat)

listFloat = [1.456, 2.125, 3.32, 4.1, 5.34]
roundFloat(listFloat)


print()
#2.6. Дан словарь: {'a': 1,'b': 2,'c': 3, 'd': 4}. Получите список его значений: [1, 2, 3, 4]
def dictInList(dictForList):
    print(list(dictForList.values()))

dictForList = {'a': 1,'b': 2,'c': 3, 'd': 4}
dictInList(dictForList)