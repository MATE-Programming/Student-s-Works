# создал функцию и у пользователя принимаю число
def summa(a = int(input())):
# 'd' мне надо на то чтоб сохранить сумму вычисления
    d = 0
# создал луп чтобы считать все числа от 1 до числа которое пользоатель ввел
    for x in range(1, a + 1):
# этот луп считать числа от 0 до значени 'x' как и было в примере
        for z in range(0, x + 1):
# создал переменную чтобы считать сумму этих чисел и сохранять
            sum = d + z
# переменный 'd' приравниваю к 'sum' чтобы кода запустился новый цыкл он добавлял именно с суммой который он считал до этого
            d = sum
# вывожу после того как все это ввычислил
    return sum
# принтанул
print(summa())