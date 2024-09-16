import turtle

# 1. Напишите программу, которая рисует прямоугольник. Примечание. Программу нужно оформить в виде функции
# rectangle(width, height), где width, height – ширина и высота прямоугольника.
def rectangle(width, height):
    turtle.showturtle()
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)

rectangle(100, 200)


# 2. Напишите программу, которая рисует правильный треугольник.
# Примечание 1. Программу нужно оформить в виде функции triangle(side), где side – длина стороны треугольника в пикселях.
# Примечание 2: Величина каждого угла правильного треугольника равна 60 градусам.
def triangle(side):
    turtle.showturtle()
    turtle.forward(side)
    turtle.setheading(120)
    turtle.forward(side)
    turtle.setheading(240)
    turtle.forward(side)

triangle(80)

# ИЛИ
def triangle(side):
    turtle.showturtle()
    n = 0
    for _ in range(4):
        turtle.forward(side)
        turtle.setheading(n+120)
        n += 120
triangle(80)


# 3. Напишите программу, которая рисует изображенную фигуру, состоящую из трех квадратов.
# Примечание 1. Напишите функцию square(side), где side – длина стороны квадрата в пикселях.
# Примечание 2. Поэксперементируйте с углом поворота черепашки при переходе от одного квадрата к другому.
def square(side):
    turtle.showturtle()
    n = 0
    for _ in range(3):
        n += 25
        turtle.setheading(n)
        for _ in range(4):
            turtle.setheading(n)
            turtle.forward(side)
            n+=90

square(80)


# 4. Напишите программу, которая рисует изображенную фигуру из восьми квадратов.
# Примечание: Используйте функцию square(side) из предыдущей задачи.
def square(side):
    turtle.showturtle()
    n = 0
    for _ in range(8):
        n += 90
        turtle.setheading(n)
        for _ in range(4):
            turtle.setheading(n)
            turtle.forward(side)
            n += 90
        n += 45

square(80)


# 5. Напишите программу, которая рисует правильный шестиугольник.
# Примечание 1. Программу нужно оформить в виде функции hexagon(side), где side – длина стороны в пикселях.
# Примечание 2. Величина каждого угла правильного шестиугольника равна 120 градусам.
def hexagon(side):
    turtle.showturtle()
    n = 0
    for _ in range(6):
        turtle.setheading(n)
        turtle.forward(side)
        n += 60

turtle.speed(10)
hexagon(80)

# ИЛИ
def hexagon(side):
    turtle.showturtle()
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

hexagon(80)


# 6. Напишите программу, которая рисует соты.
# Подсказка. Убедись, что функция рисования шестиугольника возвращает черепашку в исходную точку.
def hexagon(side):
    turtle.showturtle()
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)

hexagon(80)
for _ in range(5):
  turtle.forward(80)
  turtle.right(60)
  hexagon(80)


# 7. Напишите программу, которая рисует ромб с углами 60 и 120 градусов.
def rhombus(side):
    turtle.showturtle()
    for i in range(4):
        turtle.forward(side)
        turtle.left(120 if i % 2 == 0 else 60)

rhombus(80)


# 8. Напишите программу, которая рисует снежинку из 10 ромбов.
def snowflake(side):
    turtle.showturtle()
    for i in range(4):
        turtle.forward(side)
        turtle.left(60 if i % 2 == 0 else 120)

for i in range(10):
  turtle.left(36)
  snowflake(100)


# 9. Напишите программу, которая рисует лучи звезды, показанной на рисунке.
# Примечание: Используйте команды forward() и backward().
def star(side):
    turtle.showturtle()
    for i in range(12):
        turtle.forward(side)
        turtle.left(30)
        turtle.backward(side)

star(50)


# 10. Напишите программу, которая рисует правильную пятиконечную звезду.
def five_star(side):
    turtle.showturtle()
    for i in range(5):
        turtle.forward(side)
        turtle.right(144)

five_star(120)


# 11. Напишите программу, которая рисует квадраты, чтобы создать узор, показанный на рисунке.
def square(side):
    turtle.showturtle()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)

n = 10
for _ in range(10):
    turtle.setheading(90)
    square(n)
    n += 5


# 12. Напишите программу, которая рисует узор, показанный на рисунке.
def labyrinth(side):
    turtle.showturtle()
    turtle.forward(side)

n = 10
for _ in range(10):
    labyrinth(n)
    n += 3
    turtle.left(90)