# 1. Наполните множество set1 содержимым так, чтобы программа вывела {'p'}.
set1 = {'p'}
set2 = {'a', 't', 'f'}
print(set1 - set2)


# 2. Учитель проверяет домашнее задание в классе и получил следующие ответы: из n школьников у m домашнее задание съела
# собака, у k отключили свет, а p учеников постигли оба несчастья. Напишите программу, которая определяет сколько
# человек выполнило домашнее задание.
n = int(input())
m = int(input())
k = int(input())
p = int(input())
print(n-(m+k-p))


# 3. На спутнике «Восход» установлен прибор для измерения солнечной активности. Каждую минуту он передаёт в
# обсерваторию по каналу связи положительное целое число — количество энергии солнечного излучения. Для правильного
# анализа результатов нет необходимости держать повторяющиеся данные, поэтому их нужно удалить. Напишите программу,
# которая выводит максимальное количество показаний спутника, при удалении которых результат будет правильно проанализирован.
n = list(map(int, input().split()))
s = set(n)
print(len(n) - len(s))


# 4. Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, однако к
# концу игры ввиду своего возраста забывают, какие города уже называли.
# Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.
n = int(input())
lst = list(input() for i in range(n+1))
s = set(lst)
print('OK' if len(lst) == len(s) else 'REPEAT')


# 5. Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого
# списка у него есть. У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
# Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.
# На вход программе в первой строке подается натуральное число m — количество книг в домашней библиотеке Руслана.
# Во второй строке записано натуральное число n —  количество книг в списке на лето. Далее идут m строк с названиями
# книг из домашней библиотеки и n строк названий из списка на лето.
m = int(input())
n = int(input())
lst_home = [input() for i in range(m)]
lst_summer = [input() for i in range(n)]
for i in lst_summer:
    if i in lst_home:
        print('YES')
    else:
        print('NO')

# ИЛИ
m, n = int(input()), int(input())
libr = {input() for _ in range(m)}
for _ in range(n):
    if input() in libr:
        print('YES')
    else:
        print('NO')


# 6. Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. Каждый день
# Тимур решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все
# числа, которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором
# листочке все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него все
# совпадающие числа из первых двух листочков. Если такие числа есть — день удался, если общих чисел нет — Тимур считает день неудачным.
# Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался.
# На вход программе подаются две строки с числами: в первой строке числа с первого листочка, во второй — со второго.
n = set(map(int, input().split()))
m = set(map(int, input().split()))
if len(n&m) > 0:
    print(*sorted(n & m, reverse=True))
else:
    print('BAD DAY')


# 7. При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества
# кандидата, но и его память. Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их
# назвать. Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все
# числа, не добавляя лишних.Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.
# На вход программе подаются две строки с числами: в первой строке показанные кандидату, а во второй ответы кандидата.
n = set(map(int, input().split()))
m = set(map(int, input().split()))
print('YES' if n == m else 'NO')


# 8. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета.
# У руководителя школы есть списки изучающих каждый предмет. Напишите программу, позволяющую руководителю выяснить,
# сколько учеников изучает только математику.
# На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и
# информатику соответственно. Далее идут m строк — фамилии учеников, которые изучают математику и n строк с фамилиями
# учеников, изучающих информатику.
m = int(input())
n = int(input())
lst_m = set(input() for i in range(m))      #математика
lst_n = set(input() for j in range(n))      #информатика
print(len(lst_m - lst_n))


# 9. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
# У руководителя школы есть списки изучающих каждый предмет. Напишите программу, позволяющую руководителю выяснить,
# сколько учеников изучает только один предмет. На вход программе в первых двух строках подаются числа m и
# n – количества учеников, изучающих математику и информатику соответственно. Далее идут m строк — фамилии учеников,
# которые изучают математику и n строк с фамилиями учеников, изучающих информатику.
m = int(input())
n = int(input())
lst_m = set(input() for i in range(m))      #математика
lst_n = set(input() for j in range(n))      #информатика
print(len(lst_m.symmetric_difference(lst_n)))


# 10. Руководитель онлайн-школы BEEGEEK и его помощник вспоминают учеников своей школы. Для этого каждый из них
# составил список учеников, которых вспомнил. Напишите программу, которая выведет фамилии всех учеников, которых
# вспомнили руководитель и его помощник. На вход программе в первой строке подаются фамилии, записанные руководителем
# школы, а на второй строке подаются фамилии, записанные его помощником. Фамилии указываются через пробел.
m = set(input().split())
n = set(input().split())
print(*sorted(n | m))


# 11. Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих
# предмета. У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.
# На вход программе в первых двух строках подаются числа m и n – количества учеников, изучающих математику и
# информатику соответственно. Далее идут  m+n строк — фамилии учеников, изучающих математику и информатику, в произвольном порядке.
m = int(input())
n = int(input())
s = [input() for i in range(m + n)]
s_set = set(s)
len_s = len(s) - len(s_set)
if len(s_set) - len_s == 0:
    print('NO')
else:
    print(len(s_set) - len_s)


#  12. Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с
#  начала учебного года. Для каждого урока есть листок со списком присутствовавших учеников.
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.
# На вход программе в первой строке дается число m – количество уроков, проведенных с начала учебного года. Далее идёт
# m блоков строк, описывающих листки с фамилиями. На первой строке каждого блока указано количество фамилий ni,
# затем идёт n i строчек с фамилиями тех, кто был на i-ом уроке.
n = int(input())
result = set(input() for i in range(int(input())))
for i in range(n-1):
    result &= set(input() for i in range(int(input())))
print(*sorted(result), sep='\n')