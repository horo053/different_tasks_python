#1. В программе объявлен следующий список: lst = [5.4, 6.7, 10.4]
# На вход программе подаются целые числа, записанные через пробел. Необходимо прочитать эти числа и сохранить в отдельном списке digs.
# Добавить в конец списка lst список digs отдельным элементом (как вложенный). Результирующий список lst вывести на экран командой: print(lst)
lst = [5.4, 6.7, 10.4]
digs = list(map(int, input().split()))
lst.append(digs)
print(lst)


#2.На вход программе подаются три строки стихотворения (каждая с новой строки).
# Необходимо прочитать эти строки и каждую представить в виде отдельного списка слов (слова разделяются пробелом).
# Все полученные списки вложить в список lst и вывести его командой: print(lst)
str1 = list(input().split())
str2 = list(input().split())
str3 = list(input().split())
lst1 = [str1,str2,str3]
print(lst1)


#3.На вход программе подается матрица чисел из трех строк. В каждой строке числа разделяются пробелом.
# Необходимо прочитать эти числа и сохранить в виде двумерного (вложенного) списка.
# Затем, вывести на экран последний столбец этой матрицы (двумерного списка) в виде строки из трех чисел, записанных через пробел.
int1 = list(map(int, input().split()))
int2 = list(map(int, input().split()))
int3 = list(map(int, input().split()))
lst2 = [int1,int2,int3]
print(f"{lst2[0][-1]} {lst2[1][-1]} {lst2[2][-1]}")


#4.Имеется вложенный список: a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
# Как записать индексы, чтобы обратиться к элементу со значением "Истина"?
a = [True, [1, 0, ["True", ["Истина", "Ложь"], "False"]], False]
print(a[1][2][1][0])


#5.Имеется многомерный список: b = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
# Какую команду следует выполнить, чтобы удалить элемент со значением "F"?
b = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
del b[1][2][2]
print(b)


#6. В программе объявлен следующий вложенный список из трех строк:
# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"], ["Я", "Python", "выучил", "с", "каналом"], ["Балакирев", "что", "раздавал?"]]
# На вход программе подается строка, содержащее одно слово. Необходимо прочитать это слово и реализовать проверку на наличие его в списке t.
# Результат (булево True или False) вывести на экран. Решить задачу необходимо без применения условного оператора.
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
one_str = input()
print(one_str in t[0] or one_str in t[1] or one_str in t[2])