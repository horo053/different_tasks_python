#1. Объявите внешнюю функцию с именем counter_add и следующей сигнатурой: def counter_add(): ...
# В функции counter_add объявите вложенную функцию с одним параметром. При этом внешняя функция counter_add
# должна возвращать ссылку на вложенную функцию. Это и есть реализация замыкания. Вложенная функция должна увеличивать
# значение переданного аргумента (через ее единственный параметр) на 5 и возвращать вычисленный результат.
# После этого вызовите в программе функцию counter_add и результат ее работы присвойте переменной с именем cnt.
# То есть, переменная cnt будет ссылаться на вложенную функцию. Затем, вызовите внутреннюю функцию через переменную
# cnt со значением k, которое следует прочитать из входного потока командой: k = int(input())
# Выведите результат работы вложенной функции на экран.
def counter_add():
    def vl_counter_add(co=0):
        co += 5
        return co

    return vl_counter_add
k = int(input())
f = counter_add()
print(f(k))


#2. Объявите внешнюю функцию с именем counter_add и следующей сигнатурой: def counter_add(n): ...
# В функции counter_add, объявите вложенную функцию, которая имеет один параметр и увеличивает его значение на величину
# n - параметр внешней функции. При этом внешняя функция counter_add должна возвращать ссылку на вложенную функцию.
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
# То есть, переменная cnt будет ссылаться на вложенную функцию. Вызовите внутреннюю функцию через переменную
# cnt со значением k, , которое следует прочитать из входного потока командой: k = int(input())
# Выведите результат работы вложенной функции на экран.
def counter_add_two(n):
    def vl_counter_add(co=0):
        co += n
        return co
    return vl_counter_add
k = int(input())
f2 = counter_add_two(2)
print(f2(k))


#3. Реализуйте в программе следующее замыкание функций. Объявите внешнюю функцию без параметров.
# В ее теле объявите вложенную функцию с одним параметром, в который будет передаваться строка.
# При этом внешняя функция должна возвращать ссылку на вложенную функцию. Вложенная функция должна заключать переданную
# через параметр строку в тег h1 и возвращать результат. Например, подается строка "Python",
# вложенная функция должна вернуть строку: "<h1>Python</h1>"
# Далее, на вход программы поступает строка, которую следует прочитать из входного потока.
# Затем, вызовите внешнюю функцию для получения ссылки на вложенную функцию. Через эту ссылку вызовите вложенную
# функцию с передачей ей прочитанной строки. Результат работы вложенной функции выведите на экран.
def make_tag():
    def return_str_tag(st=' '):
        return f"<h1>{st}</h1>"
    return return_str_tag
str1 = input()
f3 = make_tag()
print(f3(str1))


#4. Реализуйте в программе следующее замыкание функций. Объявите внешнюю функцию с одним параметром tag,
# в который будет передаваться тег (строка). В теле внешней функции объявите вложенную функцию с одним параметром,
# в который будет передаваться строка, заключаемая в тег. При этом внешняя функция должна возвращать ссылку на
# вложенную функцию. Вложенная функция должна заключать переданную через параметр строку в тег tag, содержащийся в
# параметре внешней функции и возвращать результат. Например, подается строка "Python", параметр tag="div",
# вложенная функция должна вернуть строку: "<div>Python</div>"
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым.
# Прочитайте эти строки и вызовите внешнюю функцию с передачей ей прочитанного тега. Через ссылку на вложенную функцию
# вызовите ее с передачей ей прочитанной (второй) строки. Результат работы вложенной функции выведите на экран.
def make_tag_two(tag='div'):
    def return_str_tag(st=' '):
        return f"<{tag}>{st}</{tag}>"
    return return_str_tag
tag = input()
str1 = input()
f3 = make_tag_two(tag)
print(f3(str1))


#5. Реализуйте в программе следующее замыкание функций. Объявите внешнюю функцию с одним параметром tp,
# в который будет передаваться тип коллекции (строка). В теле внешней функции объявите вложенную функцию с
# одним параметром, которая преобразует строку (переданную через параметр) с набором целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# При этом внешняя функция должна возвращать ссылку на вложенную функцию.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
# вторая - последовательность целых чисел, записанных через пробел. Прочитайте их и с помощью реализованного замыкания
# преобразуйте эти данные в соответствующую коллекцию. Результат работы вложенной функции
# (сохраненный через переменную lst) выведите на экран командой: print(lst)
def make_list(tp=""):
    def return_list(stri=""):
        if tp == 'list':
            lst = [int(i) for i in stri.split()]
            return lst
        else:
            tup = tuple([int(i) for i in stri.split()])
            return tup
    return return_list
type = input()
k = input()
f = make_list(type)
print(f(k))
