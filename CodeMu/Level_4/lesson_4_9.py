#9.1. Сформируйте с помощью циклов следующий список: [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]
def generateList(stroka,stolb):
    lst_big = []
    for i in range(stroka):
        lst_small = []
        for j in range(1,stolb+1):
            if i == j:
                lst_small.append(j)
            elif i > j:
                lst_small.append(j+3)
        lst_big.append(lst_small)
    print(lst_big)

stroka,stolb = 3,3
generateList(stroka,stolb)