a = [(1, 2, 3), (3, 4, 5), (6, 7, 8)]
# создал инпут чтобы пользователь ввел число
e = int(input())
# создал цыкл чтоб пройти по всем значениям внутри списка "a"
for x in a:
# создал переменную чтобы "x" превратить в список
    dist = list(x)
# беру последнее значение и его приравниваю к числу который пользователь ввел
    dist[-1] = e
# "x" приравниваю к "dist" и его превращаю в кортеж
    x = tuple(dist)
# принтанул внутри цыкла чтобы во всех индексах последнее число изменился
    print(x, end=" ")