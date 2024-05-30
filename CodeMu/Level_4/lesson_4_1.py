#1.1. Дано некоторое число. Проверьте, что цифры этого числа расположены по возрастанию.
def intV(int_v):
    str_int = list(str(int_v))
    sort_str = sorted(str_int)
    if str_int == sort_str:
        print("по возрастанию")
    else: print("не по возрастанию")

int1,int2 = 123456, 4562789
intV(int1)
intV(int2)


#1.2. Дан список: [1, '', 2, 3, '', 5]. Удалите из списка все пустые строки.
def delNullStr(lst1):
    for i in lst1[::-1]:
        if i == '': lst1.remove(i)
    print(lst1)

lst1 = [1, '', 2, 3, '', 5]
delNullStr(lst1)


#1.3. Дан список: [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]. Выведите в консоль все элементы этого списка.
def allElementList(lst_in_lst):
    for i in lst_in_lst:
        for j in i:
            print(j)

lst_in_lst = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]
allElementList(lst_in_lst)