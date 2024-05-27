#3.1. Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.
def startLatterEndLatter(one_str, two_str):
    if one_str[-1:] == two_str[:1]: print(f"Слово '{two_str}' начинается на ту же букву, на которую заканчивается слово '{one_str}'")
    else: print(f"Первая буква в слове '{two_str}' отличается от последней буквы слова '{one_str}'")

str_one,str_two,str_three = 'торт', 'трон', 'корм'
startLatterEndLatter(str_one, str_two)
startLatterEndLatter(str_two, str_three)