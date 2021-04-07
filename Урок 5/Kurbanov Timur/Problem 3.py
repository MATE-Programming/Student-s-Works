class Bankomat:
    balance = 0

    def deposit(self):
        self.money = float(input('Введите сумму для депозита: '))
        if self.money > 0:
            self.balance += self.money
            print("Внесенная сумма: {}".format(self.money))
        else:
            print('Incorrect Input!')

    def withdrawal(self):
        self.money = float(input('Введите сумму вывода: '))
        if self.balance >= self.money and self.money > 0:
            self.balance -= self.money
            print("Вы сняли: {}".format(self.money))
        elif self.money <= 0:
            print('Incorrect Input!')
        else:
            print('Недостаточно средств!')

    def send(self):
        self.another_card = input('Введите Банковский аккаунт получателя карты: ')
        self.money = float(input('Введите сумму отправки: '))
        if self.balance >= self.money and self.money > 0:
            self.balance -= self.money
            print("Вы отправили: {}".format(self.money))
        elif self.balance <= 0:
            print('Incorrect Input!')
        else:
            print('Недостаточно средств!')

my_card = Bankomat()

while True:
    print("Добро пожаловать в банкомат Академии!", end='\n\n')

    dict = {
        1: 'Просмотр баланса',
        2: 'Внесение денег',
        3: 'Снятие денег',
        4: 'Отправка денег',
        5: 'Завершить операцию'
    }

    for key, value in dict.items():
        print(key, '-', value)

    print("")

    temp = int(input('Выберите операцию который вы хотите сделать: '))

    if(temp == 1):
        print('')
        print("Текущий баланс: {}".format(my_card.balance))
        print('')
    elif(temp == 2):
        print('')
        my_card.deposit()
        print('')
    elif(temp == 3):
        print('')
        my_card.withdrawal()
        print('')
    elif(temp == 4):
        print('')
        my_card.send()
        print('')
    elif(temp == 5):
        print('')
        print('Спасибо за выбор банкомат Академии!')
        break
    else:
        print('')
        print("Incorrect input!")
        print('')