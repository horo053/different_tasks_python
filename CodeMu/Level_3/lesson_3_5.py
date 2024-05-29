#5.1. Дан текст со словами. Запишите в список все слова, начинающиеся на букву 'a'.
def oneSymbolA(text):
    list_test = text.split(' ')
    list_new = []
    for i in list_test:
        if i[0] in 'aAаА': list_new.append(i)
    print(list_new)

text = 'смола арбуз утка Анекдот лодка кот apple'
oneSymbolA(text)


print()
#5.2. Дан список с числами. Проверьте, что все элементы этого списка являются положительными числами.
def numMoreZero(list_num):
    count = 0
    for i in list_num:
        if i < 0: count += 1
    if count > 0: print(f'{list_num} - в списке есть {count} отрицательных чисел')
    else: print(f'{list_num} - в списке отсутсвуют отрицательные числа')

list_otr, list_pol = [6,3,8,-2,-567,-56,3,-65],[5,8,3,2,0]
numMoreZero(list_otr)
numMoreZero(list_pol)


print()
#5.3. Даны два списка: lst1 = [1, 2, 3, 4, 5] и lst2 = [4, 5, 6, 7, 8]. Получите список их общих элементов: [4, 5]
def intForList(lst1,lst2):
    list_end = []
    for i in lst1:
        if i in lst2: list_end.append(i)
    print(list_end)

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
intForList(lst1,lst2)


print()
#5.4. Дана некоторая переменная с числом: num = 5; Сделайте строку, содержащую столько нулей, сколько указано в
# переменной. В нашем случае получится такая строка: '00000'
def rangeZero(num):
    list_end = []
    for i in range(1,num+1):
        list_end.append("0")
    print(''.join(list_end))
num = 5
rangeZero(num)