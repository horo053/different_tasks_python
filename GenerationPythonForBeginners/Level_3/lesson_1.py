#1. Напишите программу, которая выводит прямоугольник, по периметру состоящий из звёздочек (*).
print('*****************')
print('*               *')
print('*               *')
print('*****************')


#2. Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы (a+b)**2 и сумму квадратов
# a**2 + b**2 этих чисел в следующем формате:
# Квадрат суммы <a> и <b> равен <квадрат суммы a и b>
# Сумма квадратов <a> и <b> равна <сумма квадратов a и b>
a = int(input())
b = int(input())
print('Квадрат суммы ' + str(a) + ' и ' + str(b) + ' равен ' + str((a+b)**2))
print('Сумма квадратов ' + str(a) + ' и ' + str(b) + ' равна ' + str(a**2 + b**2))


#3. Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования.
# Напишите программу, которая считывает четыре целых положительных числа a,b,c и d и выводит на экран значение
# выражения a**b + c**d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b)+(c**d))


#4. Напишите программу, которая считывает целое положительное число n, n ∈ [1;9] и выводит значение числа n + nn + nnn
n = int(input())
print(n * 123)