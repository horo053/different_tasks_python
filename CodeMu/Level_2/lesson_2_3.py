#3.1. Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.
def startLatterEndLatter(oneStr, twoStr):
    if oneStr[-1:] == twoStr[:1]: print(f"Слово '{twoStr}' начинается на ту же букву, на которую заканчивается слово '{oneStr}'")
    else: print(f"Первая буква в слове '{twoStr}' отличается от последней буквы слова '{oneStr}'")

strOne,strTwo,strThree = 'торт','трон','корм'
startLatterEndLatter(strOne,strTwo)
startLatterEndLatter(strTwo,strThree)