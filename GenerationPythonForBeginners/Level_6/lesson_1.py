# 1. Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь:
# S = 1/2 * a * b
a = float(input())
b = float(input())
print((1/2)*a*b)


# 2. Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч. Определите, через какое время
# (в часах) старушки встретятся, если расстояние между ними равно S км.
s = float(input())
v1 = float(input())
v2 = float(input())
print(s/(v1+v2))


# 3. Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое
# с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
s = float(input())
if s == 0:
    print('Обратного числа не существует')
else:
    print(s**-1)


# 4. У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу,
# которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.
# Для получения градусов по Цельсию из градусов по Фаренгейту используйте следующую формулу:  tc = 5/9 (tF-32)
# где tF - температура в градусах по Фаренгейту.
s = float(input())
print((5/9)*(s - 32))


# 5. На вход программе подаётся число n – количество собачьих лет. Напишите программу, которая вычисляет возраст
# собаки в человеческих годах по следующему алгоритму: в течение первых двух лет собачий год равен
# 10.5 человеческим годам, после этого каждый год собаки равен 4 человеческим годам.
n = float(input())
if n <= 2:
    print(n * 10.5)
else:
    print(int((2 * 10.5) + ((n - 2) * 4)))


# 6. Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
x = float(input())
print(int(x * 10) % 10)


# 7. Дано положительное действительное число. Выведите его дробную часть.
x = float(input())
print(x - int(x))


# 8. Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число = ' + str(min(a, b, c, d, e)))
print('Наибольшее число = ' + str(max(a, b, c, d, e)))


# 9. Напишите программу, которая упорядочивает три числа от большего к меньшему.
a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) - (max(a, b, c)) - (min(a, b, c))
print(max(a, b, c))
print(s)
print(min(a, b, c))


# 10. Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней
# по величине цифре. Напишите программу, которая определяет, интересное число или нет. Если число интересное,
# следует вывести «Число интересное», иначе – «Число неинтересное».
x = int(input())
a = x // 100
b = (x // 10) % 10
c = x % 10
if max(a,b,c) - min(a,b,c) == (a+b+c) - max(a,b,c) - min(a,b,c):
    print('Число интересное')
else:
    print('Число неинтересное')


# 11. Даны пять чисел a1, a2, a3, a4, a5. Напишите программу, которая вычисляет сумму их модулей |a1| + |a2| + |a3| + |a4| + |a5|
a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))


# 12. Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути. Если только вы не
# умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# На плоскости манхэттенское расстояние между двумя точками (p1; p2) и (q1; q2) определяется так: |p1 - q1| + |p2 - q2|
# Напишите программу, определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
p1, p2, q1, q2 = (int(input()), int(input()), int(input()), int(input()))
print(abs(p1 - q1) + abs(p2 - q2))
