#8.1. Дан кортеж с числами: (1, 2, 3, 4, 5). Найдите сумму элементов этого кортежа.
def sumTuple(tupleInt):
    l = 0
    for n in tupleInt:
        l += n
    print(l)

tupleInt = (1, 2, 3, 4, 5)
sumTuple(tupleInt)


print()
#8.2. Дан список с числами:[1, 2, 3, 4, 5, 6]. Увеличьте каждое число из списка на 10 процентов.
def sumList(listInt):
    l = []
    for n in listInt:
        l.append(n + n*0.1)
    print(l)

listInt = [1, 2, 3, 4, 5, 6]
sumList(listInt)


print()
#8.3. Дана строка: 'abcdef'. Получите первых три символа этой строки: 'abc'
def threeLetter(listStr):
    print(listStr[0:3])

listStr = 'abcdef'
threeLetter(listStr)