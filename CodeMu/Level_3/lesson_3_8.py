#8.1. Дан список со числами. Проверьте, что все числа из этого списка содержат в себе цифру 3.
def listWithThree(list_three):
    count = 0
    for i in list_three:
        if '3' in str(i): count += 1
    if count == len(list_three): print(list_three, '- в списке все чиста с тройкой')
    else: print(list_three, '- в списке не все числа с тройкой')

list_with_tree, list_not_three = [3, 8523, 5437432, 335], [564,687,12367,75]
listWithThree(list_with_tree)
listWithThree(list_not_three)


print()
#8.2. Через запятую написаны числа. Получите максимальное из этих чисел.
def maxNum(list_int):
    max = 0
    for i in list_int:
        if max <= i: max = i
    print(max, '- максимальное число из списка')

list_int = [3, 8523, 5437432, 335]
maxNum(list_int)


print()
#8.3. Дана строка в формате: 'kebab-case'. Преобразуйте ее в формат: 'snake_case'
def fixStrKebab(str1):
    list_str = str1.split('-')
    list_str[0] = 'snake'
    print('_'.join(list_str))

str1 = 'kebab-case'
fixStrKebab(str1)


print()
#8.4. Дана строка в формате: 'snake_case'. Преобразуйте ее в формат: 'camelCase'
def fixStrSnake(str2):
    list_str = str2.split('_')
    list_str[0] = 'camel'
    list_str[1] = list_str[1].capitalize()
    print(''.join(list_str))

str2 = 'snake_case'
fixStrSnake(str2)


print()
#8.5. Дана строка в формате: 'camelCase'. Преобразуйте ее в формат: 'snake_case'
def fixStrCamel(str3):
    list_str = str3.split("l")
    list_str[0] = 'snake'
    list_str[1] = list_str[1].lower()
    print('_'.join(list_str))

str3 = 'camelCase'
fixStrCamel(str3)