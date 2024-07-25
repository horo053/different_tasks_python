# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код
from district.central_street.house1 import room1 as cr1, room2 as cr2
from district.soviet_street.house1 import room1 as sr1, room2 as sr2
print(*cr1.folks, sep=', ')
print(*cr2.folks, sep=', ')
print(*sr1.folks, sep=', ')
print(*sr2.folks, sep=', ')