#10.1. Дан список и число. Оставьте в списке только те числа, которые являются делителями заданного числа.
def listAndDiv(list_int,num):
    for i in list_int:
        if i % num != 0: list_int.remove(i)
    print(list_int)

list_int = [10, 4, 45, 678, 4040, 9, 450, 530001]
num = 5
listAndDiv(list_int,num)


print()
#10.2. Дан список с числами. После каждого однозначного числа вставьте еще такое же.
def listAddOne(list_one):
    list_new = []
    for i in list_one:
        if i // 10 == 0:
            list_new.append(i)
            list_new.append(i)
        else: list_new.append(i)
    print(list_new)

list_one = [10, 4, 45, 678, 4040, 9, 450, 530001]
listAddOne(list_one)


print()
#10.3. Даны два числа. Получите список цифр, которые есть и в одном, и во втором числе.
def numWithInt(int1,int2):
    set_int = set()
    for i in str(int1):
        if i in str(int2): set_int.add(int(i))
    print(list(set_int))

int1,int2 = 5964423, 7811249
numWithInt(int1,int2)


print()
#10.4. Дано число. Получите список позицией всех цифр 3 в этом числе, за исключением первой и последней.
def intWithThree(int_three):
    list_index = []
    list_int = str(int_three)
    for index, item in enumerate(list_int):
        if '3' == item and index != 0 and index != len(list_int)-1: list_index.append(index)
    print(list_index)

int3 = 396344323
intWithThree(int3)


print()
#10.5. Дан список с числами. Оставьте в нем числа, состоящие из разных цифр, а остальные удалите.
def delNum(list_num):
    count = 0
    for i in list_num:
        list_new = [item for item in str(i)]
        set_new = set(list_new)
        if len(list_new) != len(set_new): list_num.remove(i)
    print(list_num)

list_num = [3,34,765,52345,951,878]
delNum(list_num)


print()
#10.6. Даны два списка: lst1 = [1, 2, 3] и lst2 = [1, 2, 3, 4, 5];
# Удалите из большего списка лишние элементы с конца так, чтобы длины списков стали одинаковыми.
def delElementList(lst1,lst2):
    big_list = []
    small_list = []
    if len(lst1) > len(lst2):
        big_list = lst1
        small_list = lst2
    else:
        big_list = lst2
        small_list = lst1
    for i in big_list[::-1]:
        if i not in small_list: big_list.remove(i)
    print("Больший список изменен:", big_list)
    print("Меньший список", small_list)

lst1 = [1, 2, 3];
lst2 = [1, 2, 3, 4, 5];
delElementList(lst1,lst2)


print()
#10.7. Дан список с некоторыми числами, например, вот такой: [123, 456, 789]
# Напишите код, который перевернет числа в этом списке по следующему принципу: [321, 654, 987]
def reversIntInList(list1):
    list_str = [str(item) for item in list1]
    for index, i in enumerate(list_str):
        list_str[index] = i[::-1]
    list1 = [int(item) for item in list_str]
    print(list1)

list1 = [123, 456, 789]
reversIntInList(list1)