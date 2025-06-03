from datetime import date

#1. Дополните приведенный ниже код, чтобы он вывел текущую дату в ISO формате (YYYY-MM-DD).
print(date.today())


#2. Ураган Эндрю, обрушившийся на Флориду 24 августа 1992 года, был одним из самых дорогостоящих и смертоносных
# ураганов в истории США. Дополните приведенный ниже код, чтобы он вывел день недели (начиная с 0),
# в который ураган Эндрю достиг берегов США.
hurricane_andrew = date(1992, 8, 24)
print(hurricane_andrew.weekday())


#3. На Флориду с 1950 по 2017 год всего обрушилось 235 ураганов. В переменной florida_hurricane_dates хранится
# список дат, в которые произошел ураган. Сезон ураганов в Атлантике официально начинается 1 июня.
# Дополните приведенный ниже код, чтобы он вывел количество ураганов с 1950 года, которые обрушились на
# Флориду до официального начала сезона ураганов (с начала года до 1 июня не включительно).
# счетчик для нужного количества ураганов
early_hurricanes = 0
florida_hurricane_dates = [date(1992, 1, 24)]
# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)


#4. Вам доступен список dates, содержащий даты. Дополните приведенный ниже код, чтобы он вывел год и номер
# квартала каждой даты из данного списка. Компоненты дат должны быть расположены в исходном порядке,
# каждые на отдельной строке, в следующем формате: <год>-Q<номер квартала>
dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25),
         date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13),
         date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19),
         date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]
for i in dates:
    if i.month in [1,2,3]:
        print(f'{i.year}-Q{1}')
    if i.month in [4,5,6]:
        print(f'{i.year}-Q{2}')
    if i.month in [7,8,9]:
        print(f'{i.year}-Q{3}')
    if i.month in [10,11,12]:
        print(f'{i.year}-Q{4}')


#5. Реализуйте функцию get_min_max(), которая принимает один аргумент: dates — список дат (тип date)
# Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates,
# вторым — максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.
dates = [date(2021, 10, 5), date(1992, 6, 10),
         date(2012, 2, 23), date(1995, 10, 12)]

def get_min_max(dates):
    if dates:
        return min(dates), max(dates)
    return tuple()

print(get_min_max(dates))


#6. Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно.
# Если start > end, функция должна вернуть пустой список.
def get_date_range(start, end):
    sd = start.toordinal()
    ed = end.toordinal()
    if start == end:
        return [start]
    if start < end:
        return [date.fromordinal(i) for i in range(sd, ed+1)]
    return list()

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')


#7. Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
# start — начальная дата, тип date
# end — конечная дата, тип date
# Функция должна возвращать количество суббот между датами start и end включительно.
def saturdays_between_two_dates(start, end):
    start, end = sorted([start, end])
    lst = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
    return sum([1 for i in lst if i.weekday() == 5])

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))