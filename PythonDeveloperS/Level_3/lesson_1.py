import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(point, radius, sd.COLOR_CYAN, 2)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bubble(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius, color, 2)

point = sd.get_point(300, 300)
bubble(point, 12, sd.COLOR_YELLOW)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(200, 1200, 100):
    point = sd.get_point(x, 100)
    bubble(point, 7, sd.COLOR_GREEN)


# Нарисовать три ряда по 5 пузырьков
# TODO здесь ваш код
for y in range(100, 301, 100):
    for x in range(300, 800, 100):
        point = sd.get_point(x, y)
        bubble(point, 10, sd.COLOR_ORANGE)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    bubble(point, 1, sd.COLOR_PURPLE)
sd.pause()