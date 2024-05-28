#6.1. Дана некоторая строка с буквами и цифрами. Получите список позиций всех цифр из этой строки.
def strWithIntInList(str_in_list):
    if (any(character.isdigit() for character in str_in_list)):
        str = (character.isdigit() for character in str_in_list)
        list_str = list(str)
        list_index = []
        for index, item in enumerate(list_str):
            if item == True: list_index.append(index)
        print(list_index)
    else:print('В строке нет чисел')

str_with_int_one,str_with_int_two = 'rdffs47rgdkrmgd3gd', 'rgrdfgrd'
strWithIntInList(str_with_int_one)
strWithIntInList(str_with_int_two)


print()
#6.2. Дана некоторая строка:'AbCdE'. Смените регистр букв этой строки на противоположный. В нашем случае должно получится следующее: 'aBcDe'
def inverseUppInStr(str_upp):
    res = ''
    for index, item in enumerate(str_upp):
        if index % 2 == 0: res += item.lower()
        else: res += item.upper()
    print(res)

str_upp = 'AbCdE'
inverseUppInStr(str_upp)


print()
#6.3. Дан некоторый список с числами, например, вот такой: [1, 2, 3, 4, 5, 6]. Слейте пары элементов вместе: [12, 34, 56]
def joinItemInList(list_one):
    list_chet_index = []
    list_nechet_index = []
    end_list = []
    ind = 0
    for index, item in enumerate(list_one):
        if index % 2 == 0: list_chet_index.append(str(item))
        else: list_nechet_index.append(str(item))
    while len(list_chet_index) > ind and len(list_nechet_index) > ind:
        end_list.append(list_chet_index[ind] + list_nechet_index[ind])
        ind += 1
    print(list(int(item) for item in end_list))

list_one = [1, 2, 3, 4, 5, 6]
joinItemInList(list_one)


print()
#6.4. Дана некоторая строка со словами: 'aaa bbb ccc eee fff'. Сделайте заглавным первый символ каждого второго слова в этой строке. В нашем случае должно получится следующее: 'aaa Bbb ccc Eee fff'
def upperElement(str_one):
    list_str = str_one.split(' ')
    list_up = []
    for index, item in enumerate(list_str):
        if index % 2 != 0: list_up.append(item.capitalize())
        else: list_up.append(item)
    print(' '.join(list_up))

str_one = 'aaa bbb ccc eee fff'
upperElement(str_one)