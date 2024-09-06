# 1. Дополните приведенный код, чтобы в переменной result хранился словарь, в котором ключи – числа от 1 до 15
# (включительно), а значения представляют собой квадраты ключей
result = {}
for num in range(1,16):
    result[num] = result.get(num, num) ** 2
print(result)


# 2.  Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2: если ключ есть в обоих
# словарях, добавьте его в результирующий словарь со значением, равным сумме соответствующих значений из первого и
# второго словаря; если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим
# значением. Результирующий словарь необходимо присвоить переменной result.
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for key in dict1:
    if key not in dict2:
        result[key] = dict1[key]

for key in dict2:
    if key not in dict1:
        result[key] = dict2[key]

for key in dict1:
    if key in dict2:
        result[key] = dict1[key] + dict2[key]

print(result)

# ИЛИ
result = dict1.copy()

for k, v in dict2.items():
    result[k] = result.get(k, 0) + v


# 3. Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки
# text будет подсчитано количество его вхождений.
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for key in text:
    result[key] = result.get(key, 0) + 1
print(result)


# 4. Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
# должно быть выведено то, что меньше в лексикографическом порядке.
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot ' \
    'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate ' \
    'barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot ' \
    'currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant ' \
    'orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
d = dict()
for i in s:
    d[i] = d.get(i, 0) + 1
d = sorted(d.items(), key=lambda item: item[1])
print(d[-1][0])


# 5. Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж
# вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца). Дополните приведенный код так, чтобы в
# переменной result хранился словарь, в котором для каждого владельца будут перечислены его собаки. Ключом словаря
# должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек собак (сохранив исходный порядок следования).
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
result = {}
for i in pets:
    result[(i[1], i[2], i[3])] = []
for i in pets:
    for key in result:
        if (i[1], i[2], i[3]) == key:
            result[key].append(i[0])
print(result)


# 6. На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже
# всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
s = [i.strip('.,!?;:-').lower() for i in input().split()]
d = {}
lst = []
for i in s:
    d[i] = d.get(i, 0) + 1
d = sorted(d.items(), key=lambda item: item[1])
min = d[0][1]
for i in d:
    if i[1] == min:
        lst.append(i[0])
lst.sort()
print(lst[0])


# 7. На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
# постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.
s = input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
    if d[i] > 1:
        print(f'{i}_{d[i]-1}', end=' ')
    else:
        print(i, end=' ')