# 1. Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием
# и высотой равными 15 и 8 соответственно
def draw_triangle():
    for i in range(8):
        print(' '*(8-(i+1)), '*'*i, '*' * (i+1), sep='')

draw_triangle()


# 2. Интернет-магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и 120 рублей
# за каждый последующий товар. Напишите функцию get_shipping_cost(quantity), которая принимает в качестве аргумента
# натуральное число quantity – количество товаров в заказе – и возвращает стоимость доставки.
def get_shipping_cost(quantity):
    s = 0
    if quantity > 0:
        s += 1000
        for i in range(quantity-1):
            s += 120
    return s

n = int(input())

print(get_shipping_cost(n))


# 3. Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и
# возвращает значение биномиального коэффициента, равного n! / (k!(n−k)!)
# Примечание. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа, или воспользуйтесь
# уже готовой функцией из модуля math. Обратите внимание, что функция compute_binom(n, k) должна возвращать целое число.
import math

def compute_binom(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

n = int(input())
k = int(input())

print(compute_binom(n, k))


# 4. Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num
# и возвращает его словесное описание на русском языке. Примечание 1. Считайте, что число 1 ≤ num ≤ 99
import num2words
def number_to_words(num):
    return num2words.num2words(num, lang="ru")

n = int(input())

print(number_to_words(n))

# or
def number_to_words(num):
    list_num = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_num_10 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
                   'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_num_20 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 1 <= num <= 10:
        return list_num[num-1]
    if 11 <= num <= 19:
        return list_num_10[(num-10)-1]
    if 20 <= num <= 99:
        s = num//10
        k = num%10
        if k != 0:
            return f"{list_num_20[s-2]} {list_num[k-1]}"
        else:
            return list_num_20[s - 2]

n = int(input())

print(number_to_words(n))


# 5. Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru
# или en и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.
def get_month(language, number):
    ru_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
                'декабрь']

    en_month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                'november', 'december']

    if language == 'ru':
        return ru_month[number-1]
    if language == 'en':
        return en_month[number-1]

lan = input()
num = int(input())

print(get_month(lan, num))


# 6. Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.
# Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление корректной даты и
# возвращает значение True, если дата является магической и False - в противном случае.
def is_magic(date):
    end_d = date[-2:]
    date = date.split('.')
    s = int(date[0]) * int(date[1])
    if s == int(end_d):
        return True
    else:
        return False

date = input()

print(is_magic(date))


# 7. Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов,
# чтобы можно было в одной фразе рассмотреть все глифы. Напишите функцию is_pangram(text), которая принимает в качестве
# аргумента строку текста на английском языке и возвращает значение True, если текст является панграммой, или значение
# False в противном случае. Примечание 1. Гарантируется, что введённая строка содержит только буквы английского алфавита и пробелы.
def is_pangram(text):
    text = text.lower()
    alp = 'qwertyuiopasdfghjklzxcvbnm'
    c = 0
    for i in alp:
        if i in text:
            c += 1
    if c == 26: return True
    else: return False

text = input()

print(is_pangram(text))
