#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append("отец")
my_family.append("матушка")
my_family.append("дедушка")
my_family.append("бабушка")

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
]
my_family_height.append(["Александр", 185])
my_family_height.append(["Анна", 172])
my_family_height.append(["Аркадий", 179])
my_family_height.append(["Мария", 167])

# Выведите на консоль рост члена семьи в формате
#   Рост член семьи - ХХ см
print(f'Рост {my_family[0]} - {my_family_height[0][1]} см')
print(f'Рост {my_family[1]} - {my_family_height[1][1]} см')
print(f'Рост {my_family[2]} - {my_family_height[2][1]} см')
print(f'Рост {my_family[3]} - {my_family_height[3][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
all_hight = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print(f"Общий рост моей семьи - {all_hight} см")
