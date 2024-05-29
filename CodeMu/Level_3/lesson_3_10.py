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
