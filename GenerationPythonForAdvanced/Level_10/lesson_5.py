# 1. Дополните приведенный код, используя генератор, так чтобы получить словарь result, в котором ключом будет
# позиция числа в списке numbers (начиная с 0), а значением – его квадрат.
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {k: numbers[k]**2 for k in range(len(numbers))}
print(result)


# 2. Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря
# colors, кроме тех, у которых значением является None.
colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange',
          'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber',
          'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None,
          'c22': 'Sand', 'c23': None}
result = {k:v for k,v in colors.items() if v is not None}
print(result)


# 3. Дополните приведенный код, используя генератор, чтобы получить словарь result, состоящий из всех элементов словаря
# favorite_numbers, значения которых являются двузначными числами.
favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
                    'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
                    'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
                    'anna': 55, 'madlen': 876}
result = {k:v for k,v in favorite_numbers.items() if 9 < v < 100}
print(result)


# 4. Дополните приведенный код, используя генератор, так, чтобы получить словарь result, состоящий из всех элементов
# словаря months, в которых ключ и значение поменялись местами.
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}
result = {v:k for k,v in months.items()}
print(result)


# 5. В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор, чтобы получить
# словарь result, в котором числа будут ключами, а слова – значениями.
# Примечание: Ключи словаря должны быть целыми числами (иметь тип int), значения – строками (иметь тип str).
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(k):v for k,v in [i.split(':') for i in s.split()]}
print(result)


# 6. Используя генератор, дополните приведенный код, чтобы получить словарь result, где ключом будет элемент списка
# numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1.
