#1.1. С помощью включения создайте следующий список: [1, 2, 3, 4, 5, 6]
def generateList(range_list):
    print(list(item for item in range(1,range_list+1)))

range_list = 6
generateList(range_list)


print()
#1.2. Даны два списка: lst1 = [1, 2, 3] и lst2 = [4, 5, 6]. Объедините эти списки в один:[1, 2, 3, 4, 5, 6]
def joinList(one_list, two_list):
    print(one_list+two_list)

lst1,lst2 = [1, 2, 3],[4, 5, 6]
joinList(lst1,lst2)


print()
#1.3. Дан некоторый список, например, вот такой:[1, 2, 3, 4, 5, 6]. Найдите сумму первой половины элементов этого списка.
def sunElementList(list_sum):
    sum = 0
    index = 0
    while len(list_sum) // 2 > index:
        sum += list_sum[index]
        index += 1
    print(sum)

list_sum = [1, 2, 3, 4, 5, 6]
sunElementList(list_sum)