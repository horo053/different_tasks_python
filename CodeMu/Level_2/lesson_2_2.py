#2.1. Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
def countNegativeNumber(count_neg):
    count_num=0
    for n in count_neg:
        if n < 0: count_num += 1
    print(count_num)

list_int = [-1, 4, 35, -654, -446]
countNegativeNumber(list_int)


print()
#2.2. Дан список с числами. Оставьте в нем только положительные числа.
def listPositiveNum(list_positive):
    need_items = [item for item in list_positive if item < 0]
    print(need_items)

listPositiveNum(list_int)


print()
#2.3. Дана строка. Удалите предпоследний символ из этой строки.
def delStrSymbol(del_str):
    list_str = list(del_str)
    list_str.pop(-1)
    print(''.join(list_str))

del_str = 'asdfgh'
delStrSymbol(del_str)


print()
#2.4. Дан список со строками. Оставьте в этом списке только те строки, которые заканчиваются на .html.
def htmlStr(html_s):
    list_with_html = [el for el in html_s if el.endswith('.html')]
    print(list_with_html)

list_str_html = ['fdgdgr.html', 'dfgg.grhr', 'xcvbvcn.html', 'tfhtffh']
htmlStr(list_str_html)


print()
#2.5. Дан список с дробями: [1.456, 2.125, 3.32, 4.1, 5.34]
def roundFloat(list_float):
    l = 0
    while l < len(list_float):
        list_float[l] = round(list_float[l], 1)
        l += 1
    print(list_float)

list_float = [1.456, 2.125, 3.32, 4.1, 5.34]
roundFloat(list_float)


print()
#2.6. Дан словарь: {'a': 1,'b': 2,'c': 3, 'd': 4}. Получите список его значений: [1, 2, 3, 4]
def dictInList(dict_for_list):
    print(list(dict_for_list.values()))

dict_for_list = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dictInList(dict_for_list)