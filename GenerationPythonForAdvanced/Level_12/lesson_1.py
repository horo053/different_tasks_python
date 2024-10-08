import random

# 1. Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход
# количество попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).
n = int(input())
lst = ['Орел', 'Решка']
for i in range(n):
    print(random.choice(lst))


# 2. Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 6 гранями.
# Программа принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано
# на грани кубика (каждое на отдельной строке).
n = int(input())
for _ in range(n):
    print(random.randrange(1, 7))


# 3. Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
# пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).
# Примечание 1: Символам A..Z английского языка соответствуют номера с 65 по 90 в таблице символов ASCII.
# Примечание 2: Символам a..z английского языка соответствуют номера с 97 по 122 в таблице символов ASCII.
# Примечание 3: Используйте функцию chr() для получения символа по его номеру в таблице символов ASCII.
s = ''
for _ in range(int(input())):
    if random.randint(0,1) == 0:
        s += chr(random.randint(65, 90))
    else:
        s += chr(random.randint(97, 122))
print(s)


# 4. Лотерейный билет содержит 7 чисел из диапазона от 1 до 49 (включительно). Напишите программу, которая с помощью
# модуля random генерирует 7 различных случайных чисел для лотерейного билета. Программа должна вывести числа в порядке
# возрастания на одной строке через один символ пробела.
lst = [random.randint(1, 50) for _ in range(7)]
lst.sort()
print(*lst)