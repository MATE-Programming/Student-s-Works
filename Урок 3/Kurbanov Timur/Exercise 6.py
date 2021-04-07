panel = (
    "1. Зарегистрировать студента",
    "2. Удалить студента с базы данных",
    "3. Получить список студентов",
    "0. Завершить"
)

choice = 1
counter = 1
database = dict()

while(choice):

    for element in panel:
        print(element)

    print()
    choice = int(input("Введите число пункта чтобы получить информацию: "))

    check = 1

    while(check):
        if choice > 3:
            choice = int(input("Меню состоит из трёх пунктов! Введите число пункта чтобы получить информацию: "))
        elif choice < 0:
            choice = int(input("Меню состоит из трёх пунктов! Введите число пункта чтобы получить информацию: "))
        else:
            check = 0

    if choice == 1:

        print()
        print("Регистрация студента")

        name = str(input('Введите имя студента: '))
        age = int(input('Введите возраст студента: '))
        id = str(input('Введите id студента: '))
        print()

        database[str(counter) + ' студент'] = {
            'name': name,
            'age': age,
            'id': id
        }
        counter += 1

    elif choice == 2:

        print()
        print("Удаление студента из базы данных")

        temp = str(input('Введите имя студетна которого хотите удалить из базы данных: '))
        for data in list(database.keys()):
            if database[data]["name"] == temp:
                del database[data]

    elif choice == 3:

        print()
        print("Получить список студентов:")

        for data in database:
            print(data)
            print("Имя студента: " + database[data]['name'])
            print("Возраст: " + str(database[data]['age']))
            print("ID: " + str(database[data]['id']), end='\n\n')