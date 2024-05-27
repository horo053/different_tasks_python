#10.1. Дана строка: 'abcdef'. Получите каждый второй символ этой строки:
def twoLetterInStr(listStr):
    print(listStr[::2])

listStr = 'abcdef'
twoLetterInStr(listStr)


print()
#10.2. Дано некоторое число: 12345. Выведите в консоль все его символы с конца.
def symbolWithEnd(listInt):
    while listInt > 0:
        print(listInt%10)
        listInt //= 10

listInt = 12345
symbolWithEnd(listInt)