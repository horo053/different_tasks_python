#4.1. Выведите в консоль все целые числа от 1 до 100.
def nulHundred(x):
    listNum = []
    for n in range(1,x+1):
        listNum.append(n)
    print(listNum)

nulHundred(100)


print()
#4.2. Выведите в консоль все целые числа от -100 до 0.
def minHundredNul(y):
    listNum = []
    for n in range(y,1):
        listNum.append(n)
    print(listNum)

minHundredNul(-100)


print()
#4.3. Выведите в консоль все целые числа от 1 до 100.
def ontHundred(z):
    listNum = []
    for n in range(z,0,-1):
        listNum.append(n)
    print(listNum)

ontHundred(100)


print()
#4.4. Выведите в консоль все четные числа из промежутка от 1 до 100.
def oneHundredChet(ch):
    listNum = []
    for n in range(2,ch+1,2):
        listNum.append(n)
    print(listNum)

oneHundredChet(100)


print()
#4.5. Выведите в консоль все числа кратные трем в промежутке от 1 до 100.
def oneHundredThree(th):
    listNum = []
    for n in range(3,th+1,3):
        listNum.append(n)
    print(listNum)

oneHundredThree(100)


print()
#4.6. Дан список:[1, 2, 3, 4, 5, 6]. Получите из него два последних элемента:[5, 6]
def twoAndList(l):
    print(l[-2:])

listEnd = [1, 2, 3, 4, 5, 6]
twoAndList(listEnd)


print()
#4.7. Дана некоторая строка:'abcdeabc'. Получите сет ее символов:{'a', 'b', 'c', 'd', 'e'}
def strSet(strS):
    print(set(strS))

strS = 'abcdeabc'
strSet(strS)
