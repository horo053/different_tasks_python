#2.1. Дано число. Выведите в консоль первую цифру этого числа
def numberStart(x):
    if x < 0: print("Число отрицательное, первая цифра числа", str(x)[1])
    else: print("Первая цифра числа:", str(x)[0])

a,b,c,d = 22,0,-1,-354
numberStart(a)
numberStart(b)
numberStart(c)
numberStart(d)


print()
#2.2. Дано число. Выведите в консоль последнюю цифру этого числа.
def numberEnd(y):
    print("Первая цифра числа:", str(y)[-1])

numberEnd(a)
numberEnd(b)
numberEnd(c)
numberEnd(d)


print()
#2.3. Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
def numberStartEnd(z):
    if z == 0: print("Передан 0")
    elif z < 0 and z > -10: print(f"Число однозначное = {str(z)[1]}")
    elif z < 9 and z > 0: print(f"Число однозначное = {str(z)[0]}")
    elif z < -9: print(f"Первая цифра числа = {str(z)[1]}, последняя цифра числа = {str(z)[-1]}")
    elif z > 9: print(f"Первая цифра числа = {str(z)[0]}, последняя цифра числа = {str(z)[-1]}")

numberStartEnd(a)
numberStartEnd(b)
numberStartEnd(c)
numberStartEnd(d)


print()
#2.4. Дано число. Выведите количество цифр в этом числе.
def countNumber(cn):
    print("Количество цифр в строке:", len(str(abs(cn))))

countNumber(a)
countNumber(b)
countNumber(c)
countNumber(d)


print()
#2.5. Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
def oneNumber(on_one, on_two):
    if str(abs(on_one))[0] == str(abs(on_two))[0]: print(f"Первые цифры чисел {on_one} и {on_two} совпадают, и равны {str(abs(on_one))[0]}")
    else: print(f"Первые цифры чисел {on_one} и {on_two} не совпадают")

e,f,j,h = 512,59635,1023,4015
oneNumber(e,f)
oneNumber(j,h)


print()
#2.5. Дан список:[1, 2, 3, 4, 5, 6]. Получите из него следующий срез: [1, 2, 3]. То есть получить первые 3 элемента списка
def srez(list_s):
    print(list_s[0:3])

list_s = [1, 2, 3, 4, 5, 6]
srez(list_s)