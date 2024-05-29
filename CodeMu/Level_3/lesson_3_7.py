#7.1. Дана строка. Сделайте заглавной последнюю букву каждого слова в этой строке.
def upperEndLatter(str1):
    rev_str = str1[::-1]
    big_str = rev_str.title()
    str_o = big_str[::-1]
    print(str_o)

str1 = 'точка кран гранат колесница'
upperEndLatter(str1)


print()
#7.2. Дана строка. Проверьте, что эта строка состоит только из четных цифр.
def onlyChetNum(str_int):
    count = 0
    for i in str_int:
        if i not in ('2','4','6','8'): count += 1
    if count == 0: print(f'Строка "{str_int}" состоит только из четных цифр')
    else: print(f'В строке "{str_int}" есть не только четные цифры, но и нечетные цифры (и возможно буквы)')

num_str, not_num_list, num_chet_str = '45645485685', 'tfh66jghvn', '2468'
onlyChetNum(num_str)
onlyChetNum(not_num_list)
onlyChetNum(num_chet_str)


print()
#7.3. Даны две строки: txt1 = '12345' и txt2 = '45678'. Получите символы, которые есть и в одной, и в другой строке:
def twoStrHasElement(txt1,txt2):
    res = ''
    for i in txt1:
        if i in txt2: res += i
    print("Одинаковые символы в обоих строках:", res)

txt1 = '12345'
txt2 = '45678'
twoStrHasElement(txt1,txt2)


print()
#7.4. Дана некоторая строка: 'a bc def ghij'. Переведите в верхний регистр все подстроки, в которых количество букв
# меньше или равно трем. В нашем случае должно получится следующее: 'A BC DEF ghij'
def upperMoreThreeWorld(str2):
    list_str = str2.split(' ')
    for index, n in enumerate(list_str):
        if len(n) <= 3: list_str[index] = n.upper()
    print(list_str)

str2 = 'a bc def ghij'
upperMoreThreeWorld(str2)