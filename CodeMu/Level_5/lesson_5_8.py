#8.1. Попросите пользователя ввести год. Получите в список дат всех пятниц 13-е в введенном году.
import datetime
def friday13(year):
    count = 0
    start_year = datetime.datetime.strptime(f"{year}-01-01", "%Y-%m-%d")
    end_year = datetime.datetime.strptime(f"{year}-12-31", "%Y-%m-%d")
    while start_year < end_year:
        if start_year.day == 13 and start_year.isoweekday() == 5:
            count += 1
        start_year = start_year + datetime.timedelta(days=1)
    print(count)

year = input("Введите год: ")
friday13(year)


#8.2. Дана строка со словами. Отсортируйте слова в алфавитном порядке.
import datetime
def sortWorld(str1):
    lst = str1.split()
    lst.sort()
    print(' '.join(lst))

str1 = "слово буква символ число"
sortWorld(str1)


#8.3. Дана строка с датой: '2025-2-1' Напишите код, который при необходимости добавит нули к месяцу и дню: '2025-02-01'
import datetime
def addNullInDate(date_not_have_null):
    full_date = datetime.datetime.strptime(date_not_have_null, "%Y-%m-%d")
    print(full_date.date())

date_not_have_null = '2025-2-1'
addNullInDate(date_not_have_null)


#8.4. Напишите программу, которая сформирует следующую строку:
import datetime
def generateStr(count_int):
    res = ''
    for i in range(1, count_int+1):
        res = res + '-' + str(i)
    print(res + '-')

count_int = 5
generateStr(count_int)

