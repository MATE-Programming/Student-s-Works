print("""
    Инструкция
Введите любое положительное число 
Если введете счисло '0' или отрицательное число
то выполучите треугольники со зведочками
с высотой данными вами числами
""")
# создал лист чтобы сюда добавлять числа которые пользоатель введкт ниже
list = []
# создал цыкл чтобы он повторно ввел пока он не вводит 0 или отрицательное число
while True:
# получаю от пользователя число
    x = int(input('Введите число: '
                  ''))
# добавляю в список, как сказал выше
    list.append(x)
# если введет число 0 или меньше то цыкл остановится
    if x <= 0:
        break
# создал переменную для нового цыкла
i = 0
# а это переменная для того чтоб считал длину листа
h = 1
# создал цыкл от 0 до длины листа
while i <= len(list):
# переменный per приравниваю к значению в листе с индексом i
    per = list[i]
# создал функцию из-за того что это было дз без функции б был намного проще
    def func(x):
# создал цыкл for чтобы взять все числа от 1 до значению в листе с индексом i
      for z in range(1, list[i] + 1):
# создал переменную чтобы сохранить и его вычисление, а он вычисляет точнее омножает звездочку к числу z в цыкле for
          num = '*' * z
# полученный с вычислением выше сохраненным переменным принтую
          print(num)
# созданный выше функию даю значение per
    func(per)
# я задал в эту переменную 1 из-за того что функция len(list) cчитает не от 0 а от 1
    h += 1
# проверяю: если i меньше len(list) то есть длины листа и отнимаю еденицу 1 из-за того что как сказал выше len(list) cчитает не от 0 а от 1
    if i < len(list) - 1:
# если условеие истина то к i добавляю еденицу 1
        i += 1
# если переменный h равен к длину листа то остановит цыкл, добавил ееницу из-за того что надо добавить и все 😅
    if h == len(list) + 1:
        break