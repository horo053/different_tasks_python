#4.1. Дан список с числами. Оставьте в нем только те числа, которые делятся на 5.
def listNumDivFive(str_int):
    for i in str_int[::-1]:
        if i%5 != 0: str_int.remove(i)
    print(str_int)

str_int = [3,5,7,43,3245,55,767,1230,345436,5464562343240]
listNumDivFive(str_int)


print()
#4.2. Дано число. Проверьте, что у этого числа есть только один делитель, кроме него самого и единицы.
def oneDel(int_for_del):
    count = 0
    for i in range(1,int_for_del+1):
        if int_for_del % i == 0: count += 1
    if count == 3: print("У числа один делитель")
    else: print('У числа несколько делителей')

int1,int2 = 4, 15313
oneDel(int1)
oneDel(int2)


print()
#4.3. Дан следующий словарь: dct = { 1: { 1: 11, 2: 12, 3: 13, }, 2: { 1: 21, 2: 22, 3: 23, }, 3: { 1: 24, 2: 25, 3: 26, }, }
# Найдите сумму элементов этого словаря.
def sumDict(dct):
    sum = 0
    for i in dct.values():
        for j in i.values():
            sum += j
    print(sum)

dct = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}
sumDict(dct)