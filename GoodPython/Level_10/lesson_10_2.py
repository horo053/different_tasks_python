# 2. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции,
# включите третий бит введенного числа. Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено: 11010001
n = int(input())
n = n|8
print(n)


# 3. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции,
# выключите 4-й и 1-й биты введенного числа. Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено: 11010001
n = int(input())
n = n & ~0b10010
print(n)


# 4. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции,
# переключите 3-й и 0-й биты введенного числа. Выведите на экран полученное числовое значение.
# P. S. Распределение номеров бит представлено: 11010001
n = int(input())
n = n ^ 0b1001
print(n)


# 5. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции,
# выполните умножение введенного числа на 4. Выведите на экран полученное числовое значение.
n = int(input())
n = n << 2   #умножение на 4
print(n)


# 6. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции, выполните
# целочисленное деление введенного числа на 2. Выведите на экран полученное числовое значение.
n = int(input())
n = n >> 1   #деление на 2
print(n)


# 7. На вход программе подается зашифрованное слово. Шифрование кодов символов этого слова было проведено с помощью
# битовой операции XOR с ключом key=123. То есть, каждый символ был преобразован по алгоритму:
# x = ord(x) ^ key
# Здесь ord - функция, возвращающая код символа x. Прочитайте слово из входного потока и расшифруйте его.
# Выведите на экран результат расшифровки.
n = input()
for i in n:
    print(chr(ord(i) ^ 123), end='')


# 8. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции, проверьте,
# включен ли 6-й и 3-й биты введенного числа. Если они оба включены, то выведите слово "ДА", иначе - слово "НЕТ".
# P. S. Распределение номеров бит представлено: 11010001
n = input()
if n & (1 << 3) and n & (1 << 6):
    print('ДА')
else:
    print('НЕТ')


# 9. На вход программе подается целое десятичное число. Прочитайте его и, используя битовые операции, проверьте,
# включен ли 5-й или 1-й биты введенного числа. Если включен хотя бы один из этих битов, то выведите слово "ДА", иначе - слово "НЕТ".
# P. S. Распределение номеров бит представлено
n = int(input())
if n & (1 << 1) or n & (1 << 5):
    print('ДА')
else:
    print('НЕТ')