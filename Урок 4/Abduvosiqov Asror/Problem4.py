# создал функци и задал нанего 4 значения
def f(x, a, b, c):
# и создал переменную 'sum' и вычислил по формуле
    sum = a * (x**2) + b * x + c
# послетого как вычислил я выожу значение 'sum'
    return sum
# принтанул функцию и внутри фунции я получаю от пользователя числа для 'x' , 'a' , 'b' , 'c'
print(f(x=int(input('Введие число "x": ')), a=int(input('Введие число "a": ')),b=int(input('Введие число "b": ')), c=int(input('Введие число "c": '))))