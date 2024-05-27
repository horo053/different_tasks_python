#10.1. Дана строка: 'abcdef'. Получите каждый второй символ этой строки:
def twoLetterInStr(list_str):
    print(list_str[::2])

list_str = 'abcdef'
twoLetterInStr(list_str)


print()
#10.2. Дано некоторое число: 12345. Выведите в консоль все его символы с конца.
def symbolWithEnd(list_int):
    while list_int > 0:
        print(list_int % 10)
        list_int //= 10

list_int = 12345
symbolWithEnd(list_int)