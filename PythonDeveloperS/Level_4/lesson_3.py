# Создать модуль my_burger. В нем определить функции добавления ингредиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера
# с помощью фукций из my_burger и вывести на консоль.

# TODO здесь ваш код
from my_burger import my_burger
my_burger.add_bun()
my_burger.add_mayonnaise()
my_burger.add_cutlet()
my_burger.add_cheese()
my_burger.add_bun()
my_burger.add_mayonnaise()
my_burger.add_cutlet()
my_burger.add_cheese()
my_burger.add_cucumber()
my_burger.add_tomato()
my_burger.add_bun()
print(my_burger.my_burger)

