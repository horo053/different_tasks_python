#4.1. Попросите пользователя ввести целое число через консоль. Получите факториал введенного числа.
def factorialInt(int1):
    mul = 1
    try:
        int(int1) == float(int1)

        for i in range(1,int(int1)+1):
            mul *= i
        print(mul)

    except:
        print("Не целое число")

int1 = input("Введите целое число: ")
factorialInt(int1)


print()
# 4.2. Напишите программу, которая сформирует следующую строку: '-1-2-3-4-5-'
def generateStr(int2):
    res = ''
    for i in range(1,int2+1):
        res = res + '-' + str(i)
    print(res+'-')

int2 = 5
generateStr(int2)


print()
# 4.3. Дана некоторая строка: '1 22 333 4444 22 5555 1'
# Удалите из этой строки все подстроки, в которых количество символов больше трех. В нашем случае должно получится следующее:
# '1 22 333 22 1'
def delElementThree(str1):
    list_str = str1.split(' ')
    for i in list_str[::-1]:
        if len(i) > 3: list_str.remove(i)
    print(' '.join(list_str))

str1 = '1 22 333 4444 22 5555 1'
delElementThree(str1)