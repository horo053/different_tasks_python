# 1. Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
for i in range(10):
    print('Python is awesome!')


# 2. Дано предложение и количество раз, сколько его надо повторить. Напишите программу, которая повторяет
# данное предложение нужное количество раз.
a = input()
b = int(input())
for i in range(b):
    print(a)


# 3. Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:AAA
# AAA
# AAA
# AAA
# AAA
# AAA
# BBBB
# BBBB
# BBBB
# BBBB
# BBBB
# E
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# TTTTT
# G
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


# 4. На вход программе подается натуральное число n. Напишите программу, которая печатает звездный прямоугольник размерами n*19
n = int(input())
for i in range(n):
    print('*' * 19)


# 5. Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9,
# каждая с указанной строкой текста.
n = input()
for i in range(10):
    print(i, n)


# 6. На вход программе подаётся натуральное число n. Напишите программу, которая для каждого из чисел от 0 до n
# (включительно) выводит текст в следующем формате: Квадрат числа <текущее число> равен <квадрат текущего числа>
n = int(input())
for i in range(n + 1):
    print(f'Квадрат числа {i} равен {i**2}')


# 7. На вход программе подаётся натуральное число n(n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звёздный треугольник в соответствии с примером.
n = int(input())
for i in range(n):
    print('*' * (n - i))


# 8. На вход программе подаются три натуральных числа m, p, n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов с 1-го по n-й день (включительно).
# Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.
m, p, n = float(input()), float(input()), int(input())
a = 0
for i in range(n):
    print(i + 1, m)
    m = m + m * p / 100