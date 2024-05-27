#9.1. Дана строка: 'abcdef'. Получите три последних символа этой строки: 'def'
def threeLetter(listStr):
    print(listStr[3:])

listStr = 'abcdef'
threeLetter(listStr)


print()
#9.2. Дан словарь с числами: {'a': 1,'b': 2,'c': 3, 'd': 4}. Увеличьте каждое число из словаря в 2 раза
def dictValue(listStr):
    for key in listStr:
        listStr[key] *= 2
    print(listStr)

dictInt = {'a': 1,'b': 2,'c': 3, 'd': 4}
dictValue(dictInt)