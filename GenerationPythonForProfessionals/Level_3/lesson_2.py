from datetime import date, time

#1. Вам доступно время alarm. Дополните приведенный ниже код, чтобы он вывел следующие его компоненты:
# количество часов в формате HH
# количество минут в формате MM
# количество секунд в формате SS
alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))


#2. Вам доступна дата birthday. Дополните приведенный ниже код, чтобы он вывел следующие её компоненты:
# полное название месяца на английском
# полное название дня недели на английском
# год в формате YYYY
# номер месяца в формате MM
# день месяца в формате DD
birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))


#3. В переменной florida_hurricane_dates хранится список дат (тип date), в которые произошел ураган во Флориде
# с 1950 по 2017 год. Дополните приведенный ниже код, чтобы он вывел самую раннюю дату из списка
# florida_hurricane_dates в трех различных форматах:
# в стандарте ISO (YYYY-MM-DD)
# в типичном для России стиле (DD.MM.YYYY)
# в типичном для Америки стиле (MM/DD/YYYY)
# присваиваем самую раннюю дату урагана в переменную first_date
florida_hurricane_dates = [date(1992, 10, 6)]
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%Y-%m-%d')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)


#4. Ураган Эндрю, который обрушился на Флориду 24 августа 1992 года, был одним из самых дорогостоящих и
# смертоносных ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел дату 24 августа
# 1992 года в трех различных форматах:
# в формате YYYY-MM
# в формате month_name (YYYY), где month_name – полное название месяца на английском
# в формате YYYY-day_number, где day_number – день года
andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


#5. Напишите программу, которая принимает на вход две даты и выводит ту, что меньше.
year1, month1, day1 = input().split('-')
year2, month2, day2 = input().split('-')

my_date1 = date(int(year1), int(month1), int(day1))
my_date2 = date(int(year2), int(month2), int(day2))

min_date = min(my_date1, my_date2)
print(min_date.strftime('%d-%m (%Y)'))

# ИЛИ
date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())

print(min(date1, date2).strftime('%d-%m (%Y)'))


#6. Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.
n = int(input())
date_list = [input() for _ in range(n)]
date_list.sort()
for i in date_list:
    date_form = date.fromisoformat(i)
    print(date_form.strftime('%d/%m/%Y'))


#7. Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и
# номера дня равна его возрасту. Год рождения Тимура — 1992, возраст — 29 лет.
# Реализуйте функцию print_good_dates(), которая принимает один аргумент:
# dates — список дат (тип date)
# Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате
# month_name DD, YYYY, где month_name — полное название месяца на английском.
def print_good_dates(dates):
    dates.sort()
    for i in dates:
        if i.year == 1992 and (i.month + i.day) == 29:
            print(i.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)


#8. Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
# day — натуральное число, день
# month — натуральное число, месяц
# year — натуральное число, год
# Функция должна возвращать True, если дата с компонентами day, month и year является корректной,
# или False в противном случае.
def is_correct(day, month, year):
    try:
        my_date = date(int(year), int(month), int(day))
        return True
    except:
        return False

print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))


#9. Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except:
        return False

count = 0
date_full = input()

while date_full != 'end':
    day, month, year = date_full.split('.')
    if is_correct(int(day), int(month), int(year)):
        count += 1
        print('Корректная')
    else:
        print('Некорректная')
    date_full = input()
print(count)

#ИЛИ
count = 0
for i in iter(input, 'end'):
    try:
        date(*map(int, i.split('.')[::-1]))
        print('Корректная')
        count += 1
    except:
        print('Некорректная')

print(count)