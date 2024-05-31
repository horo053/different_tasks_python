#3.1. Попросите пользователя ввести два числа целых числа через консоль.
# Заполните список целыми числами от минимального введенного числа до максимального.
from datetime import datetime
from datetime import date
import calendar


def listMinMax(int1,int2):
    min_list = [int(int1),int(int2)]
    list_new = []

    for i in range(min(min_list), max(min_list)+1):
        list_new.append(i)
    print(list_new)

int1 = input("Введите первое целое число: ")
int2 = input("Введите второе целое число: ")
listMinMax(int1,int2)


print()
#3.2. Попросите пользователя ввести дату в формате год-месяц-день. Определите день недели, соответствующий этой дате.
def dayWeekInDate(date1):
    try:
        datetime.strptime(date1, "%Y-%m-%d").date()

        date_list = date1.split('-')
        date2 = [int(item) for item in date_list]
        day_in_week = date(date2[0], date2[1], date2[2])
        if day_in_week.isoweekday() == 1: print('Понедельник')
        elif day_in_week.isoweekday() == 2: print('Вторник')
        elif day_in_week.isoweekday() == 3: print('Среда')
        elif day_in_week.isoweekday() == 4: print('Четверг')
        elif day_in_week.isoweekday() == 5: print('Пятница')
        elif day_in_week.isoweekday() == 6: print('Суббота')
        elif day_in_week.isoweekday() == 7: print('Воскресенье')
    except:
        print("Число не соответсвует формату")


date1 = input("Введите дату в формате 'год-месяц-день': ")
dayWeekInDate(date1)


print()
#3.3. Попросите пользователя ввести год. Определите, високосный этот год или нет.
def foolYear(year):
    int_year = int(year)
    if calendar.isleap(int_year):
        print("Год високосный")
    else: print("Год не високосный")

year = input("Введите год: ")
foolYear(year)


print()
#3.4. Напишите программу, которая сформирует следующую строку: '54321'
def generaateStr(int3):
    res = ''
    for i in range(int3,0,-1):
        res = res + str(i)
    print(res)


int3 = 5
generaateStr(int3)


print()
#3.5. Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]. Поменяйте местами пары элементов этого списка: [2, 1, 4, 3, 6, 5]
def revList(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    print(lst)

lst = [1, 2, 3, 4, 5, 6]
revList(lst)