# 5.1. Попросите пользователя ввести дату рождения в формате год-месяц-день. Определите, сколько полных лет пользователю.
import datetime

def countYears(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d').date()

        dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        today = datetime.date.today()
        print(((today - dt.date()).days)//365)
    except:
        print("Не соответсвует формату")

date = input("Введите дату рождения: ")
countYears(date)


print()
# 5.2. Попросите пользователя ввести три числа. Проверьте, что эти числа являются тройкой Пифагора: квадрат самого большого числа должен быть равен сумме квадратов двух остальных.
def trianglePif(int1,int2,int3):
    list_int = [int(int1),int(int2),int(int3)]
    s = max(list_int)
    list_int.remove(max(list_int))
    if s ** 2 == list_int[0]**2 + list_int[1]**2: print("Треугольник Пифагора")
    else: print("Не треугольник Пифагора")

int1 = input("Введите первое число: ")
int2 = input("Введите второе число: ")
int3 = input("Введите третье число: ")
trianglePif(int1,int2,int3)


print()
# 5.3. Дано некоторое число: 35142. Отсортируйте цифры этого числа. В нашем случае должно получится следующее: 12345

def sortInt(int4):
    int_str = str(int4)
    sort_str = sorted(int_str)
    print(int(''.join(sort_str)))

int4 = 35142
sortInt(int4)