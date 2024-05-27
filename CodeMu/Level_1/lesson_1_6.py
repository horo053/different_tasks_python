#6.1. Дан список с числами:[1, 2, 3, 4, 5]. Найдите сумму элементов этого списка.
def listSum(list_s):
    s = 0
    for n in list_s:
        s += n
    print(s)

list_s = [1, 2, 3, 4, 5]
listSum(list_s)


print()
#6.2. Дан список с числами: [1, 2, 3, 4, 5]. Найдите сумму квадратов элементов этого списка.
def listSumQtr(list_sum_q):
    qtr = 0
    for n in list_sum_q:
        qtr += (n**2)
    print(qtr)

listSumQtr(list_s)


print()
#6.3. Дан список с числами: [1, 2, 3, 4, 5]. Найдите сумму квадратных корней элементов этого списка.
def listSumSqtr(list_sum_q):
    qtr = 0
    for n in list_sum_q:
        qtr += (n**0.5)
    print(qtr)

listSumSqtr(list_s)


print()
#6.4. Дан список с числами: [1, 2, -3, 4, -5]. Найдите сумму положительных элементов этого списка.
def listSumPositiveNum(list_pos_num):
    k = 0
    for n in list_pos_num:
        if n > 0: k += n
    print(k)

list_pos_num = [1, 2, -3, 4, -5]
listSumPositiveNum(list_pos_num)


print()
#6.5. Дан список с числами: [-1, 2, -3, 4, 5, 11]. Найдите сумму тех элементов этого списка, которые больше нуля и меньше десяти.
def listSumNullToTen(list_null_to_ten):
    l = 0
    for n in list_null_to_ten:
        if n > 0 and n < 10: l += n
    print(l)

list_null_to_ten = [-1, 2, -3, 4, 5, 11]
listSumNullToTen(list_null_to_ten)


print()
#6.6. Дана некоторая строка: 'abcde'. Переберите и выведите в консоль по очереди все символы с конца строки.
def reverseString(str_s):
    strRev = ''.join(reversed(str_s))
    for n in strRev:
        print(n)

str_s = 'abcde'
reverseString(str_s)