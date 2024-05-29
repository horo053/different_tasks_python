#3.1. Дано некоторое число: 1357. Проверьте, что все цифры этого числа являются нечетными.
def findNech(int_nech):
    list_int = list(str(int_nech))
    count = 0
    for i in list_int:
        if int(i) % 2 != 0: count += 1
    if count == len(list_int): print(f"В числе {int_nech} все цифры нечетные")
    else: print(f"В числе {int_nech} есть четные цифры")

int_nech, int_chet = 1357,5621
findNech(int_nech)
findNech(int_chet)


print()
#3.2. Дано некоторое слово: 'abcba'. Проверьте, что это слово читается одинаково с любой стороны.
def reverseStr(str_rev):
    revers_str = str_rev[::-1]
    index = 0
    count = 0
    while index < len(str_rev) and index < len(revers_str):
        if str_rev[index] == revers_str[index]: count += 1
        index += 1
    if count == len(str_rev): print(f"Строка палиндром '{str_rev}'")
    else: print(f"Строка '{str_rev}' не является палиндромом")

str1, str2 = 'abcba','abcde'
reverseStr(str1)
reverseStr(str2)


print()
#3.3. Даны два сета: st1 = {1, 2, 3} st2 = {4, 5, 6}. Объедините эти сеты в один: {1, 2, 3, 4, 5, 6}
def joinSet(st1,st2):
    new_set = set.union(st1,st2)
    print(new_set)

st1, st2 = {1, 2, 3},{4, 5, 6}
joinSet(st1,st2)