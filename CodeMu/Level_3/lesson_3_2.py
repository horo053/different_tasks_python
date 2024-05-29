#2.1. С помощью включения создайте следующий список: [1, 3, 5, 7, 9]
def generateList(range_list):
    print([i for i in range(range_list) if i % 2])

range_list = 10
generateList(range_list)


print()
#2.2. Даны два кортежа: tpl1 = (1, 2, 3) и tpl2 = (4, 5, 6). Объедините эти кортежи в один:(1, 2, 3, 4, 5, 6)
def joinTuple(tpl1, tpl2):
    print(tpl1+tpl2)

tpl1,tpl2 = (1, 2, 3),(4, 5, 6)
joinTuple(tpl1,tpl2)


print()
#2.3. Даны два словаря: dct1 = { 'a': 1, 'b': 2, } и dct2 = { 'c': 3, 'd': 4, }. Объедините эти словари в один:{ 'a': 1, 'b': 2, 'c': 3, 'd': 4, }
def joinDict(dct1, dct2):
    new_dict = {**dct1,**dct2}
    print(new_dict)

dct1,dct2 = { 'a': 1, 'b': 2, },{ 'c': 3, 'd': 4, }
joinDict(dct1,dct2)


print()
#2.4. Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]. Поделите сумму первой половины элементов этого списка на сумму второй половины элементов.
def sumDivList(div_list):
    lst1 = div_list[:len(div_list)//2]
    lst2 = div_list[len(div_list)//2:]
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for j in lst2:
        sum2 += j
    print(i/j)

div_list = [1, 2, 3, 4, 5, 6]
sumDivList(div_list)