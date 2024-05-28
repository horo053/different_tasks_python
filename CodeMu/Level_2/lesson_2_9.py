#9.1. С помощью цикла заполните список четными числами из промежутка от 1 до 100.
def listAppendForChetNumLimit(num_limit):
    list_num_chet = []
    for i in range(1,num_limit+1):
        if i % 2 == 0: list_num_chet.append(i)
    print(list_num_chet)

num_limit = 100
listAppendForChetNumLimit(num_limit)


print()
#9.2. Дан список с числами:[1, 2, 3, 4, 5]. Выведите в консоль элементы этого списка в обратном порядке.
def reverseList(list_one):
    print(list_one[len(list_one)::-1])

list_one = [1, 2, 3, 4, 5]
reverseList(list_one)


print()
#9.3. Даны две строки: txt1 = 'abcde' и txt2 = '12345'. Сделайте из этих строк словарь так, чтобы символы первой строки
# стали ключами, а символы второй строки - значениями: { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, }
def strInDict(txt1,txt2):
    list_txt1 = list(txt1)
    list_txt2_str = txt2
    list_txt2 = list(int(item) for item in list_txt2_str)
    print(dict(zip(list_txt1,list_txt2)))

txt1,txt2 = 'abcde','12345'
strInDict(txt1,txt2)