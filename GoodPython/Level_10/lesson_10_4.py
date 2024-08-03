# 5. Пользователь может ввести с клавиатуры следующие команды в виде строки:
# top или Top или TOP
# bottom или Bottom или BOTTOM
# right или Right или RIGHT
# left или Left или LEFT
# cmd = input()
# С помощью оператора match/case необходимо определить тип команды cmd и при совпадении вывести на экран сообщение в формате:
# Команда <название команды малыми буквами>
# Например, при вводе Top, должны на выходе получить: Команда top
# И так для всех четырех команд. Если тип команды не определен, то вывести строку: Неверная команда
cmd = input()
match cmd:
    case str() as comm if comm == 'top' or comm == 'TOP' or comm == 'Top':
        print('Команда top')
    case str() as comm if comm == 'right' or comm == 'Right' or comm == 'RIGHT':
        print('Команда right')
    case str() as comm if comm == 'bottom' or comm == 'Bottom' or comm == 'BOTTOM':
        print('Команда bottom')
    case str() as comm if comm == 'left' or comm == 'Left' or comm == 'LEFT':
        print('Команда left')
    case _:
        print('Неверная команда')

#  ИЛИ
cmd = input()

match cmd.lower():
    case 'top' | 'bottom' | 'right' | 'left':
        print(f'Команда {cmd.lower()}')
    case _:
        print('Неверная команда')


# 6. В функцию get_data() передается параметр value:
# def get_data(value):
#     match value:
#         # здесь продолжайте программу
#     return None
# Необходимо дописать оператор match/case в этой функции так, чтобы для каждого типа данных (int, float и str)
# формировалась переменная со значением value и возвращалась функцией (непосредственно из блока case).
# P. S. Вызывать функцию не нужно, только дописать.
def get_data(value):
    match value:
        case str():
            return str(value)
        case int():
            return int(value)
        case float():
            return float(value)
    return None


# 7. В функцию get_data() передается параметр value:
# def get_data(value):
#     match value:
#         # здесь продолжайте программу
#     return None
# Необходимо дописать оператор match/case со следующими шаблонами:
# если переменная value имеет тип int и больше нуля, то вернуть значение переменной value;
# если переменная value имеет тип float и находится в диапазоне [-100; 100], то вернуть значение переменной value;
# если переменная value имеет тип str, то просто вернуть ее значение.
# P. S. Вызывать функцию не нужно, только дописать шаблоны.
def get_data(value):
    match value:
        case int() as v if v > 0:
            return v
        case float() as v if -100 <= v <= 100:
            return v
        case str():
            return value
    return None