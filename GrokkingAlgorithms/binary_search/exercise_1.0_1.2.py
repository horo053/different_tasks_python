def binary_search(list, item):
    low = 0
    high = len(list)-1
    k = 0                                    #Счетчик количества раз пройденного цикла

    while low <= high:
        mid = int((low + high) / 2)          #Найти серединный индекс списка
        guess = list[mid]                    #Ввести переменную с серединным значением в списке
        if guess == item:
            return f'Индекс заданного в item значения равен {mid}, счетчик цикла равен {k}'
        if guess > item:
            high = mid - 1              #(mid - 1) - потому что среднее значение уже было проверено и не подошло
        else:
            low = mid + 1
        k += 1
    return None

my_list = [i for i in range(1, 129)]
my_list_two = [i for i in range(1, (128*2)+1)]
print(binary_search(my_list, 1))
print(binary_search(my_list_two, 180))
