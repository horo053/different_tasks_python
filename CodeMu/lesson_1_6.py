#6.1. Дан список с числами:[1, 2, 3, 4, 5]. Найдите сумму элементов этого списка.
def listSum(listS):
    s = 0
    for n in listS:
        s += n
    print(s)

listS = [1, 2, 3, 4, 5]
listSum(listS)


print()
#6.2. Дан список с числами: [1, 2, 3, 4, 5]. Найдите сумму квадратов элементов этого списка.
def listSumQtr(listSumQ):
    qtr = 0
    for n in listSumQ:
        qtr += (n**2)
    print(qtr)

listSumQtr(listS)


print()
#6.3. Дан список с числами: [1, 2, 3, 4, 5]. Найдите сумму квадратных корней элементов этого списка.
def listSumSqtr(listSumQ):
    qtr = 0
    for n in listSumQ:
        qtr += (n**0.5)
    print(qtr)

listSumSqtr(listS)


print()
#6.4. Дан список с числами: [1, 2, -3, 4, -5]. Найдите сумму положительных элементов этого списка.
def listSumPositiveNum(listPosNum):
    k = 0
    for n in listPosNum:
        if n > 0: k += n
    print(k)

listPosNum = [1, 2, -3, 4, -5]
listSumPositiveNum(listPosNum)


print()
#6.5. Дан список с числами: [-1, 2, -3, 4, 5, 11]. Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.
def listSumNullToTen(listNullToTen):
    l = 0
    for n in listNullToTen:
        if n > 0 and n < 10: l += n
    print(l)

listNullToTen = [-1, 2, -3, 4, 5, 11]
listSumNullToTen(listNullToTen)


print()
#6.6. Дана некоторая строка: 'abcde'. Переберите и выведите в консоль по очереди все символы с конца строки.
def reverseString(strS):
    strRev = ''.join(reversed(strS))
    for n in strRev:
        print(n)

strS = 'abcde'
reverseString(strS)