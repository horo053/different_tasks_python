#4.1. Дана строка. Удалите из нее все гласные буквы.
def delGlLatters(str_gl):
    list_str_gl = list(str_gl)
    gl = 'eyuioaEYUIOAуеыаоэяиюУЕЫАОЭЯИЮ'
    for i in list_str_gl[::-1]:
        if i in gl: list_str_gl.remove(i)
    print(''.join(list_str_gl))

str_gl = '32syuwfmрееЯgd3AO:GE'
delGlLatters(str_gl)


print()
#4.2. Даны два сета: st1 = {1, 2, 3, 4, 5} и st2 = {4, 5, 6, 7, 8}. Получите сет их общих элементов: {4, 5}
def findNumInSet(st1,st2):
    list_set = []
    for i in st1:
        if i in st2: list_set.append(i)
    print(set(list_set))

st1 = {1, 2, 3, 4, 5}
st2 = {4, 5, 6, 7, 8}
findNumInSet(st1,st2)


print()
#4.3. Даны два сета: st1 = {1, 2, 3, 4, 5} и st2 = {4, 5, 6, 7, 8}. Получите сет элементов, входящих только в один из сетов: {1, 2, 3, 6, 7, 8}
def findNumAndDel(st3,st4):
    set_up = set.union(st3,st4)
    print(set_up)

st3 = {1, 2, 3, 4, 5}
st4 = {4, 5, 6, 7, 8}
findNumAndDel(st3,st4)

