import calendar
from datetime import date


#1. Напишите программу, которая определяет, является ли год високосным.
# n = int(input())
# lst = [int(input()) for _ in range(n)]
# for i in lst:
#     print(calendar.isleap(i))


#2. Напишите программу, которая выводит календарь на заданные год и месяц.
# year, month = input().split(' ')
# month_lst = list(calendar.month_abbr)
# print(calendar.month(int(year), month_lst.index(month)))


#3. Напишите программу, которая определяет день недели, соответствующий заданной дате.
# year, month, day = map(int, input().split('-'))
# day_week = list(calendar.day_name)[calendar.weekday(year, month, day)]
# print(day_week)


#4. Напишите программу, которая определяет количество дней в заданном месяце. 2008 1
# year, month = map(int, input().split(' '))
# count_day = calendar.monthrange(year, month)[1]
# print(count_day)


#5. Напишите программу, которая определяет количество дней в заданном месяце. 1983 January
# year, month = input().split(' ')
# num_month = list(calendar.month_name).index(month)
# count_day = calendar.monthrange(int(year), num_month)[1]
# print(count_day)


#6. Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
# year — натуральное число
# month — полное название месяца на английском
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.
def get_days_in_month(year, month):
    num_month = list(calendar.month_name).index(month)
    count_day = calendar.monthrange(int(year), num_month)[1]
    start = date(year=year, month=num_month, day=1)
    end = date(year=year, month=num_month, day=count_day)
    lst = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
    return lst

print(get_days_in_month(1982, 'January'))


#7. Реализуйте функцию get_all_mondays(), которая принимает один аргумент:
# year — натуральное число
# Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year,
# выпадающих на понедельник.
def get_all_mondays(year):
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=12, day=31)
    lst = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
    s = []
    for i in lst:
        if i.weekday() == 0:
            s.append(i)
    return s

#ИЛИ
def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays


#8. Во многих музеях существует один день месяца, когда посещение музея для всех лиц или отдельных категорий
# граждан происходит без взимания платы. Например, в Эрмитаже это третий четверг месяца.
# Напишите программу, которая определяет даты бесплатных дней посещения Эрмитажа в заданном году.
year = int(input())
for month in range(1, 13):
    for week in calendar.monthcalendar(year, month):
        t = week[3]
        if 15 <= t <= 21:
            d = date(year, month, t)
            print(date.strftime(d, '%d.%m.%Y'))