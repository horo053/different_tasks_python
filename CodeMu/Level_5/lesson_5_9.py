#8.1. Выведите в консоль название дня недели последнего дня текущего месяца.
import datetime
import calendar
def lastDayInMonth():
    year = datetime.datetime.today().year
    month = datetime.datetime.today().month
    _, last_day_in_month = calendar.monthrange(year,month)
    last_day = datetime.datetime.strptime(f"{year}-{month}-{last_day_in_month}", '%Y-%m-%d')
    if datetime.datetime.isoweekday(last_day) == 1: print("Понедельник")
    elif datetime.datetime.isoweekday(last_day) == 2: print("Вторник")
    elif datetime.datetime.isoweekday(last_day) == 3: print("Среда")
    elif datetime.datetime.isoweekday(last_day) == 4: print("Четверг")
    elif datetime.datetime.isoweekday(last_day) == 5: print("Пятница")
    elif datetime.datetime.isoweekday(last_day) == 6: print("Суббота")
    elif datetime.datetime.isoweekday(last_day) == 7: print("Воскресенье")
lastDayInMonth()



#8.2. Дана строка с текстом. Получите процентное
# содержание каждого символа текста в виде словаря, в котором ключами будут символы, а значениями - их процентное содержание.
def percentLatter(str1):
    s = {}
    for char in str1:
        if char in s:
            s[char] += 1
        else: s[char] = 1
    percentages = {char: (count / len(str1)) * 100 for char, count in s.items()}
    print(percentages)

str1 = "текст сила мышь тетрадь медведь слон"
percentLatter(str1)


#8.3. Дана некоторая строка с числом: '1234567'
# Отделите тройки цифр пробелами, начиная с конца числа. В нашем случае должно получится следующее: '1 234 567'
def threeSymbolWithEnd(str2):
    end_str = '{0:,}'.format(int(str2)).replace(',', ' ')
    print(end_str)

str2 = '1234567'
threeSymbolWithEnd(str2)

