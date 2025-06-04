import time
from datetime import timedelta, datetime, date

#1. Дополните приведенный ниже код, чтобы он прибавил к объекту datetime(2021, 11, 4, 13, 6) одну неделю
# и 12 часов и вывел результат в формате DD.MM.YYYY HH:MM:SS.
dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))


#2. Дополните приведенный ниже код, чтобы он вывел количество дней (целое число) между датами today и birthday
today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = (birthday-today).days

print(days)


#3. Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.
# Формат входных данных: На вход программе подается дата в формате DD.MM.YYYY.
# Формат выходных данных: Программа должна вывести предыдущую и следующую даты относительно введенной даты,
# каждую на отдельной строке, в формате DD.MM.YYYY.
# Примечание 1: Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.
day, month, year = input().split('.')
my_date = date(int(year), int(month), int(day))
yesterday = (my_date - timedelta(days=1)).strftime('%d.%m.%Y')
tomorrow = (my_date + timedelta(days=1)).strftime('%d.%m.%Y')
print(yesterday, tomorrow, sep='\n')

#ИЛИ
mask='%d.%m.%Y'
my_date=datetime.strptime(input(), mask)


#4. Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.
# Формат входных данных: На вход программе подается время в формате HH:MM:SS.
# Формат выходных данных: Программа должна вывести целое количество секунд, прошедшее с начала суток.
# Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.
hour, minut, sec = map(int, input().split(':'))
my_time = timedelta(hours=hour, minutes=minut, seconds=sec).seconds
print(my_time)


#5. Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через n секунд.
# Напишите программу, которая определит, какое время будет на часах, когда прозвенит таймер.
# Формат входных данных: На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS. В
# следующей строке вводится целое неотрицательное число n — количество секунд, через которое должен прозвенеть таймер.
# Формат выходных данных: Программа должна вывести время в формате HH:MM:SS, которое будет на часах,
# когда прозвенит таймер.
hour, minut, sec = map(int, input().split(':'))
n = int(input())
my_time = (datetime(1,1,1, hour, minut, sec) + timedelta(seconds=n)).time()
print(my_time)


#6. Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
# year — натуральное число, год
# Функция должна возвращать количество воскресений в году year.
def num_of_sundays(year):
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=12, day=31)
    lst = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
    s = 0
    for i in lst:
        if i.weekday() == 6:
            s += 1
    return s

print(num_of_sundays(2022))

#ИЛИ
def num_of_sundays_u(year):
    dt = datetime(year, 12, 31)
    return int(dt.strftime('%U'))

print(num_of_sundays_u(2022))


#7. Артуру нужно подготовить 10 задач для нового курса "ООП на Python".
# Чтобы занятие не оказалось утомительным, он придумал правило:
# если сегодня он подготовил первую задачу, то вторую он должен подготовить через один день
# если сегодня он подготовил вторую задачу, то третью он должен подготовить через два дня
# если сегодня он подготовил третью задачу, то четвертую он должен подготовить через три дня
# и так далее
# Напишите программу, которая определяет даты, в которые Артуру нужно подготовить задачи.
# Формат входных данных: На вход программе подается дата подготовки первой задачи в формате DD.MM.YYYY.
# Формат выходных данных: Программа должна вывести 10 дат, удовлетворяющих условию задачи,
# каждую на отдельной строке, в формате DD.MM.YYYY.
day, month, year = input().split('.')
my_date = date(int(year), int(month), int(day))
for i in range(10):
    print(my_date.strftime('%d.%m.%Y'))
    my_date += timedelta(days=i+2)


#8. Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются
# неотрицательные целые числа — количество дней между двумя соседними датами последовательности.
dates = [datetime.strptime(x, '%d.%m.%Y') for x in input().split()]
dif = [abs(dates[i] - dates[i+1]).days for i in range(len(dates) - 1)]
print(dif)


#9. Реализуйте функцию fill_up_missing_dates(), которая принимает на вход один аргумент:
# dates — список строковых дат в формате DD.MM.YYYY
# Функция должна возвращать список, в котором содержатся все даты из списка dates, расположенные в порядке
# возрастания, а также все недостающие промежуточные даты.
def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(x, pattern) for x in dates]
    start, end = min(dates), max(dates)
    days = (end - start).days + 1
    days_lst = [(start + timedelta(days=i)).strftime(pattern) for i in range(days)]
    return days_lst


#10. Репетитор по математике проводит занятия по 45 минут с перерывами по 10 минут.
# Репетитор обозначает время начала рабочего дня и время окончания рабочего дня. Напишите программу,
# которая генерирует и выводит расписание занятий.
pattern = '%H:%M'
start, end = [datetime.strptime(input(), pattern) for i in range(2)]
while (start + timedelta(minutes=45)) <= end:
    print(start.strftime(pattern), '-', (start + timedelta(minutes=45)).strftime(pattern))
    start += timedelta(minutes=55)