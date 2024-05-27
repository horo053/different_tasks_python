#1.1. Дано число. Проверьте, отрицательное оно или нет. Выведите об этом информацию в консоль
def numberCheck(x):
    if x < 0: print("Отрицательное число:", x)
    elif x > 0: print("Положительное число:", x)
    else: print("Передан 0")

a,b,c,d = 22,0,-1,-354
numberCheck(a)
numberCheck(b)
numberCheck(c)
numberCheck(d)


print()
#1.2. Дана строка. Выведите в консоль длину этой строки.
def lenStr(y):
    print("Длина строки:", len(y))

e,f,g = "23145428","Привет","Hi"
lenStr(e)
lenStr(f)
lenStr(g)


print()
#1.3. Дана строка. Выведите в консоль последний символ строки.
def endLetter(z):
    print("Последний символ строки:", z[-1])

endLetter(e)
endLetter(f)
endLetter(g)


print()
#1.4. Дано число. Проверьте, четное оно или нет.
def chetNum(ch):
    if ch == 0: print("Передан 0")
    elif ch % 2 == 0: print("Четное число:", ch)
    else: print("Нечетное число:", ch)

chetNum(a)
chetNum(b)
chetNum(c)
chetNum(d)


print()
#1.5. Даны два слова. Проверьте, что первые буквы этих слов совпадают.
def oneLatter(one_l, two_l):
    if len(one_l) == 0 or len(two_l) == 0: print("Слова не переданы")
    else:
        if one_l[0] == two_l[0]: print(f"Первые буквы у слова {one_l} и слова {two_l} одинаковые")
        else: print(f"Первые буквы у слова {one_l} и слова {two_l} разные")

h,i = "Python", "Java"
j,k = "Игра", "Икра"
l,m = "", ""
oneLatter(h,i)
oneLatter(j,k)
oneLatter(l,m)


print()
#1.6. Дано слово. Получите его последнюю букву. Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.
def endLatter(str):
    if len(str) == 0: print("Слово не передано")
    else:
        if str[-1] == "ь": print("Последняя буква мягкий знак, предпоследняя:", str[-2])
        else: print("Последняя буква:", str[-1])

n,o,p = "Морской котик","Тюлень",""
endLatter(n)
endLatter(o)
endLatter(p)