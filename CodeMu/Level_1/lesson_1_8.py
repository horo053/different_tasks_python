#8.1. Дан кортеж с числами: (1, 2, 3, 4, 5). Найдите сумму элементов этого кортежа.
def sumTuple(tuple_int):
    l = 0
    for n in tuple_int:
        l += n
    print(l)

tuple_int = (1, 2, 3, 4, 5)
sumTuple(tuple_int)


print()
#8.2. Дан список с числами:[1, 2, 3, 4, 5, 6]. Увеличьте каждое число из списка на 10 процентов.
def sumList(list_int):
    l = []
    for n in list_int:
        l.append(n + n*0.1)
    print(l)

list_int = [1, 2, 3, 4, 5, 6]
sumList(list_int)


print()
#8.3. Дана строка: 'abcdef'. Получите первых три символа этой строки: 'abc'
def threeLetter(list_str):
    print(list_str[0:3])

list_str = 'abcdef'
threeLetter(list_str)