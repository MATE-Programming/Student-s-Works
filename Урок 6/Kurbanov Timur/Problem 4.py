import os
import datetime

cheque = open('cheque.txt', mode='a+', encoding='UTF-8')

blank = {
        'show': '№{}\nТекущий баланс: ${}\n{}\n\n',
        'deposit': '№{}\nВнесённая сумма: ${}\n{}\n\n',
        'withdrawal': '№{}\nВы сняли: ${}\n{}\n\n',
        'send': '№{}\nВы отправили на карту {}: ${}\n{}\n\n'
    }

class Bank:
    balance = 0
    loop = 0

    def show(self):
        print("Текущий баланс: {}".format(self.balance))
        self.loop += 1
        print(blank['show'].format(self.loop, self.balance, datetime.datetime.now()), file=cheque)


    def deposit(self):
        self.money = int(input('Введите сумму для депозита: '))

        if self.money > 0:
            self.balance += self.money
            self.loop += 1
            print('Внесённая сумма: {}\n'.format(self.money))
            print(blank['deposit'].format(self.loop, self.money, datetime.datetime.now()), file=cheque)
        else:
            print('Incorrect Input!')

    def withdrawal(self):
        self.money = int(input('Введите сумму вывода: '))

        if self.balance >= (self.money + self.money/100) and self.money > 0:
            self.balance -= (self.money + self.money/100)
            self.loop += 1
            print(blank['withdrawal'].format(self.loop, self.money, datetime.datetime.now()), file=cheque)
            print("Вы сняли: {}".format(self.money))
        elif self.money <= 0:
            print('Incorrect Input!')
        else:
            print('Недостаточно средств!')

    def send(self):
        self.another_card = input('Введите Банковский аккаунт получателя карты: ')
        self.money = float(input('Введите сумму отправки: '))

        if self.balance >= (self.money + self.money/100) and self.money > 0:
            self.balance -= (self.money + self.money/100)
            self.loop += 1
            print("Вы отправили: {}".format(self.money))
            print(blank['send'].format(self.loop, self.another_card, self.money, datetime.datetime.now()), file=cheque)
        elif self.balance <= 0:
            print('Incorrect Input!')
        else:
            print('Недостаточно средств!')

card = Bank()

while True:
    password = str(input('Введите свой пароль для входа в ваш кошелёк или "Выход" для выхода: '))

    if(password == 'пароль'):
        os.system('cls')

        print("Добро пожаловать в банкомат Академии!", end='\n\n')

        option = {
            1: 'Просмотр баланса',
            2: 'Внесение денег',
            3: 'Снятие денег',
            4: 'Отправка денег',
            5: 'Завершить операцию'
        }

        while True:
            for key, value in option.items():
                print(key, '-', value)

            print()

            check = int(input('Выберите операцию который вы хотите сделать: '))

            if (check == 1):
                os.system('cls')
                card.show()
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')
            elif (check == 2):
                os.system('cls')
                card.deposit()
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')
            elif (check == 3):
                os.system('cls')
                card.withdrawal()
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')
            elif (check == 4):
                os.system('cls')
                card.send()
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')
            elif (check == 5):
                os.system('cls')
                print('Спасибо за выбор банкомат Академии!')
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Incorrect input!")
                input("Нажмите Enter для продолжения работы...")
                os.system('cls')

    elif(password == 'Выход' or password == 'выход'):
        break

    else:
        print('Вы ввели не верный пароль!', end="\n\n")

cheque.close()