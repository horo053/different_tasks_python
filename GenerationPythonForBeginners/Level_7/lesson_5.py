# 1. Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
n = int(input())
while n:
    print(n % 10)
    n //= 10


# 2. Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
n = int(input())
while n != 0:
    print(n % 10, end='')
    n //= 10


# 3. Дано натуральное число n(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и
# выводит текст в следующем формате:
# Максимальная цифра равна <максимальная цифра>
# Минимальная цифра равна <минимальная цифра>
x = str(input())
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))


# 4. Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
n = list(map(int, input()))
print(sum(n))
print(len(n))
mul = 1
for i in n: mul *= i
print(mul)
print(sum(n) / len(n))
print(n[0])
print(n[0] + n[-1])


# 5. Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.
n = int(input())
while len(str(n)) > 2:
    k = n % 10
    n = n // 10
n = n % 10
print(n)


# 6. Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
n = input()
if max(n) == min(n):
    print('YES')
else:
    print('NO')


# 7. Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр
# при просмотре справа налево упорядоченной по неубыванию.
n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)