# 1. Дополните приведенный код, используя индексатор, так чтобы он вывел 17-ый (по порядку) элемент списка primes.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])


# 2. Дополните приведенный код, используя индексатор, так чтобы он вывел последний элемент списка primes..
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])


# 3. Дополните приведенный код, используя срезы, так чтобы он вывел первые 6 элементов списка primes.
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])


# 4. Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка numbers.
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers) + min(numbers))


# 5. Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens.
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)


# 6. Дополните приведенный код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый,
# а элемент Violet на Фиолетовый. Далее необходимо вывести полученный список.
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)


# 7. Дополните приведенный код так, чтобы он вывел "перевёрнутый" список languages (т.е. элементы будут идти в обратном порядке).
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])


# 8. Дополните приведенный код, используя операторы конкатенации (+) и умножения списка на число (*), так чтобы он вывел список:
# [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
num = numbers1*2 + numbers2*9 + numbers3
print(num)