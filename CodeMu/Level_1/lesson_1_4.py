#4.1. Выведите в консоль все целые числа от 1 до 100.
def nulHundred(x):
    list_num = []
    for n in range(1,x+1):
        list_num.append(n)
    print(list_num)

nulHundred(100)


print()
#4.2. Выведите в консоль все целые числа от -100 до 0.
def minHundredNul(y):
    list_num = []
    for n in range(y,1):
        list_num.append(n)
    print(list_num)

minHundredNul(-100)


print()
#4.3. Выведите в консоль все целые числа от 1 до 100.
def ontHundred(z):
    list_num = []
    for n in range(z,0,-1):
        list_num.append(n)
    print(list_num)

ontHundred(100)


print()
#4.4. Выведите в консоль все четные числа из промежутка от 1 до 100.
def oneHundredChet(ch):
    list_num = []
    for n in range(2,ch+1,2):
        list_num.append(n)
    print(list_num)

oneHundredChet(100)


print()
#4.5. Выведите в консоль все числа кратные трем в промежутке от 1 до 100.
def oneHundredThree(th):
    list_num = []
    for n in range(3,th+1,3):
        list_num.append(n)
    print(list_num)

oneHundredThree(100)


print()
#4.6. Дан список:[1, 2, 3, 4, 5, 6]. Получите из него два последних элемента:[5, 6]
def twoAndList(l):
    print(l[-2:])

list_end = [1, 2, 3, 4, 5, 6]
twoAndList(list_end)


print()
#4.7. Дана некоторая строка:'abcdeabc'. Получите сет ее символов:{'a', 'b', 'c', 'd', 'e'}
def strSet(str_s):
    print(set(str_s))

str_s = 'abcdeabc'
strSet(str_s)
