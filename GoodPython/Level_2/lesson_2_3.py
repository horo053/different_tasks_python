import math
#1. Допишите текст программы для вычисления модуля введенного с клавиатуры числа в переменную d.
# Выведите результат (модуль) в консоль с помощью функции print.
#Sample Input: -5. Sample Output: 5
d = int(input())
print(abs(d))


print()
#2. Допишите текст программы для нахождения минимального значения из пяти введенных целых
# чисел с выводом результата в консоль (минимального значения) с помощью функции print
d1, d2, d3, d4, d5 = map(int, input().split())
print(min(d1, d2, d3, d4, d5))


print()
#3. Допишите текст программы для нахождения максимального значения из пяти введенных целых чисел
# с выводом результата (максимального значения) в консоль с помощью функции print.
d1, d2, d3, d4, d5 = map(int, input().split())
print(max(d1, d2, d3, d4, d5))


print()
#4. Допишите текст программы для вычисления евклидового расстояния (гипотенузы)
# по перемещениям a и b. Округлите результат с точностью до сотых.
# Полученное значение выведите на экран. Sample Input: 3 4. Sample Output: 5.0
a, b = map(int, input().split())
print(round(((a**2 + b ** 2) ** 0.5), 2))


print()
#5. Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе).
# Выведите результат в консоль в виде целого числа с помощью функции print.
# Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
# Sample Input: 6 3. Sample Output: 20
n, k = map(int, input().split())
fac = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(fac)


print()
#6. В летний лагерь нужно отвезти n детей и m вожатых с помощью автобусов (значения считываются из входного потока в программе ниже).
# Максимальная вместимость каждого автобуса 20 человек. Допишите программу для вычисления минимального числа автобусов,
# необходимых для перевозки детей вместе с вожатыми. Результат выведите в консоль в виде целого числа.
n, m = map(int, input().split())
print(math.ceil((n+m)/20))


print()
#7.Гелиевая ручка стоит x рублей (значение вводится из входного потока в программе ниже).
# Сегодня магазин предоставляет скидку в 10% на каждую купленную ручку.
# Какое наибольшее количество таких ручек можно будет купить на 500 рублей? Результат выведите в консоль в виде целого числа.
# Sample Input: 20. Sample Output: 27
x = int(input())
print(math.ceil(500 // (x * 0.9)))
