#3. Объявите в программе функцию, которая не имеет параметров и просто выводит на экран следующую строку:
def return_print():
    print("It's my first function")
return_print()


#4. Объявите в программе функцию без параметров, которая читает из входного потока (с клавиатуры) имя и фамилию,
# записанные в одну строку через пробел, и выводит на экран сообщение (без кавычек):
# "Уважаемый, <имя> <фамилия>! Вы верно выполнили это задание!"
# После объявления вызовите эту функцию.
def return_fio():
    fio = input()
    print(f"Уважаемый, {fio}! Вы верно выполнили это задание!")
return_fio()


#5.Объявите в программе функцию, которая имеет один параметр - вес предмета, и выводит на экран сообщение (без кавычек):
# "Предмет имеет вес: x кг."
# где x - переданное значение (аргумент) функции. После объявления функции прочитайте (с помощью функции input)
# вещественное число и вызовите функцию с этим числовым значением.
def return_weight(x):
    print(f"Предмет имеет вес: {x} кг.")
return_weight(input())