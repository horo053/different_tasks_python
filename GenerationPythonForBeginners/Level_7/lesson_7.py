# 1. На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке).
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и
# их произведение. Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и
# написал программу неправильно. Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка
# затрагивает только одну строку и может быть исправлена без изменения других строк.
count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')


# 2. На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). Известно, что
# вводимые числа по абсолютной величине не превышают 10**6. Нужно написать программу, которая выводит на экран сумму
# всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности.
# Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.
mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')


# 3. На обработку поступает последовательность из 7 целых чисел (каждое на отдельной строке). Нужно написать программу,
# которая подсчитывает и выводит сумму всех чётных чисел последовательности или 0, если чётных чисел в
# последовательности нет. Программист торопился и написал программу неправильно. Найдите все ошибки в этой программе
# (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
s = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)


# 4. На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную
# цифру числа, кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести «NO».
# Программист торопился и написал программу неправильно. Найдите все ошибки в этой программе (их ровно 5).
# Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)


# 5. На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую
# (старшую) цифру. Программист торопился и написал программу неправильно. Найдите все ошибки в этой программе
# (их ровно 2). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
while n > 9:
    n //= 10
print(n)


# 6. На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр
# введенного числа. Программист торопился и написал программу неправильно. Найдите все ошибки в этой программе
# (их ровно 3). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
n = int(input())
product = 1
while n :
    digit = n % 10
    product = product * digit
    n //= 10
print(product)