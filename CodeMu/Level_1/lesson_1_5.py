#5.1. Найдите сумму всех целых чисел от 1 до 100.
def sumOneToHundred(x):
    s = 0
    for n in range(1,x+1):
        s += n
    print(s)

sumOneToHundred(100)


print()
#5.2. Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
def sumChetOneToHundred(x):
    s = 0
    for n in range(2,x+1,2):
        s += n
    print(s)

sumChetOneToHundred(100)


print()
#5.3. Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
def sumNechetOneToHundred(x):
    s = 0
    for n in range(1,x+1,2):
        s += n
    print(s)

sumNechetOneToHundred(100)


print()
#5.4. Даны два целых числа. Найдите остаток от деления первого числа на второе.
def remainderOfTheDiv(ch_one, ch_two):
    print(ch_one % ch_two)

ch_one,ch_two = 19,4
remainderOfTheDiv(ch_one, ch_two)


print()
#5.5. Дан список:[1, 2, 3, 4, 5, 6]. Получите из него каждый второй элемент:[1, 3, 5]
def twoElemList(list_two_elem):
    print(list_two_elem[::2])

list_two_elem = [1, 2, 3, 4, 5, 6]
twoElemList(list_two_elem)