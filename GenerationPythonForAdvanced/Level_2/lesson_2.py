# 1. Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой
# координатной четверти. В первой строке записано количество точек. Каждая следующая строка состоит из двух целых
# чисел — координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.
n = int(input())
kp1, kp2, kp3, kp4 = 0, 0, 0, 0
for _ in range(n):
    x,y = map(int, input().split())
    if x > 0 and y > 0:
        kp1 += 1
    if x < 0 and y > 0:
        kp2 += 1
    if x < 0 and y < 0:
        kp3 += 1
    if x > 0 and y < 0:
        kp4 += 1
print(f"Первая четверть: {kp1}\n"
      f"Вторая четверть: {kp2}\n"
      f"Третья четверть: {kp3}\n"
      f"Четвертая четверть: {kp4}\n")


# 2. На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу
# подсчета количества чисел, которые больше предшествующего им в этом списке числа, то есть, стоят вслед за меньшим числом.
n = list(map(int, input().split()))
count = 0
for i in range(1,len(n)):
    if n[i-1] < n[i]:
        count += 1
print(count)


# 3. На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов, то последний остается на своем месте.
n = list(map(int, input().split()))
for i in range(len(n)-1):
    if i%2 == 0:
        n[i], n[i+1] = n[i+1], n[i]
print(*n)


# 4. На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
# а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.
n = list(map(int, input().split()))
m = []
for i in range(len(n)):
    if i == 0:
        m.append(n[-1])
    else:
        m.append(n[i-1])
print(*m)


# 5. На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.
n = list(map(int, input().split()))
count = 0
for ind, it in enumerate(n):
    if n[ind-1] != n[ind] or len(n) == 1:
        count += 1
print(count)


# 6. Напишите программу для определения, является ли число произведением двух чисел из данного набора.
# Программа должна выводить результат в виде ответа «ДА» или «НЕТ».
# В первой строке подаётся натуральное число n (0<n<1000) – количество чисел в наборе. В последующих n строках вводятся
# целые числа, составляющие набор (могут повторяться). Затем следует целое число, которое является или не является
# произведением двух каких-то чисел из набора. Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
# Примечание 1. Само на себя число из набора умножиться не может. Другими словами, два множителя должны иметь разные индексы в наборе.
# Примечание 2. Для решения задачи используйте вложенные циклы.
n = int(input())
count = 0
k = [int(i) for i in (input() for j in range(n))]
p = int(input())
for ind, it in enumerate(k):
    for jnd, jt in enumerate(k):
        if it * jt == p and ind != jnd:
            count += 1
if count > 0: print('ДА')
else: print('НЕТ')


# 7. Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть
# в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
# На первой строке записан выбор Тимура, на второй – выбор Руслана. Программа должна вывести результат жеребьёвки,
# то есть кто победит: Тимур, Руслан или же они сыграют вничью.
# Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.
t = input()
r = input()
if (t == 'камень' and r == 'камень') or (t == 'бумага' and r == 'бумага') or (t == 'ножницы' and r == 'ножницы'):
    print('ничья')
elif (t == 'камень' and r == 'ножницы') or (t == 'бумага' and r == 'камень') or (t == 'ножницы' and r == 'бумага'):
    print('Тимур')
elif (r == 'камень' and t == 'ножницы') or (r == 'бумага' and t == 'камень') or (r == 'ножницы' and t == 'бумага'):
    print('Руслан')


# 8. Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. Теперь Тимур и Руслан
# играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить,
# кто будет делать следующий модуль в новом курсе. На вход программе подаются две строки текста, содержащие по одному
# слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура,
# на второй – выбор Руслана. Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.
# Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица
# травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу,
# на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.
t = input()
r = input()
s = {'камень':['ящерица', 'ножницы'],
     'ножницы':['бумага', 'ящерица'],
     'бумага':['камень', 'Спок'],
     'ящерица':['Спок', 'бумага'],
     'Спок':['ножницы', 'камень']}
if t == r:
    print('ничья')
elif r in s.get(t):
    print('Тимур')
else:
    print('Руслан')


# 9. Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" соответствует выпадению Орла,
# а буква "Р" - выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
s = input()
c = 0
max = 0
for ind, it in enumerate(s):
    if it == 'Р':
        c += 1
        if c > max:
            max = c
    else: c = 0
print(max)


# 10. Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в
# качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
# слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен
# и нужно вывести номер холодильника, нумерация начинается с единицы.
# В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки, содержащие
# латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
'''n = int(input())
lst = [i for i in (input() for _ in range(n))]
lst_str = []
for ind, it in enumerate(lst):
    c = ''
    for jnd, jt in enumerate(it):
        if jt in 'anton' and jt != it[jnd-1]:
            c += jt
    if 'a' in c and c.count('n') > 1 and 't' in c and 'o' in c:
        lst_str.append(ind+1)
print(*lst_str)'''