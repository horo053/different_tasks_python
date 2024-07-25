# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1 import room1 as cr1, room2 as cr2
from district.soviet_street.house1 import room1 as sr1, room2 as sr2
print(f"На Центральной улице живут: {', '.join(cr1.folks)}, {', '.join(cr2.folks)}")
print(f"На Советской улице живут: {', '.join(sr1.folks)}, {', '.join(sr2.folks)}")