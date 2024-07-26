# 1. Напишите программу, которая выводит текст:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
print('"Python is a great language!", said Fred. ' + '"I ' + "don't " + 'ever remember having this much fun before."')


# 2. Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# Hello <введённое имя> <введённая фамилия>! You have just delved into Python
a = input()
b = input()
print(f"Hello {a} {b}! You just delved into Python")


# 3. Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит
# информацию о ней в следующем формате: Футбольная команда <название футбольной команды>
# имеет длину <длина названия футбольной команды> символов.
a = input()
print(f"Футбольная команда {a} имеет длину {len(a)} символов")


# 4. Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
a, b, c = input(), input(), input()
if min(len(a), len(b), len(c)) == len(a):
    if max(len(b), len(c)) == len(b):
        print(a)
        print(b)
    else:
        print(a)
        print(c)
elif min(len(a), len(b), len(c)) == len(b):
    if max(len(a), len(c)) == len(a):
        print(b)
        print(a)
    else:
        print(b)
        print(c)
elif min(len(a), len(b), len(c)) == len(c):
    if max(len(a), len(b)) == len(a):
        print(c)
        print(a)
    else:
        print(c)
        print(b)


# 5. Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
# можно ли из длин этих строк построить арифметическую прогрессию.
a,b,c=input(),input(),input()
a1=len(a)
b1=len(b)
c1=len(c)
if ((2*b1-c1-a1)*(2*c1-b1-a1)*(2*a1-b1-c1)) == 0:
    print('YES')
else:
    print('NO')


# 6. Напишите программу, которая считывает одну строку, после чего выводит «YES»,
# если во введённой строке есть подстрока «синий», или «NO» в противном случае.
s = input()
if 'синий' in s:
    print('YES')
else:
    print('NO')


# 7. Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек),
# если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.
s = input()
if 'суббота' in s:
    print('YES')
elif 'воскресенье' in s:
    print('YES')
else:
    print('NO')


# 8. Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.).
# Напишите программу, проверяющую корректность email адреса.
s = input()
if '@' in s and '.' in s:
    print('YES')
else:
    print('NO')