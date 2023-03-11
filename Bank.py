import random
a = 0
i = 0
azb = ["a","b","c","d","e","f","g","u","j","k","l","m","n","o","p","r","s","t","y","z","w","1","2","3","4","5","6","7","8","9"]
class Bank():

    def __init__(self,balance,acc_numb):
        self.balance = balance
        self.acc_numb = acc_numb

    def deposit(self,deposit):
        self.deposit = int(deposit)
        if self.balance > self.deposit:
            self.balance -= self.deposit
            print(f'Вы сняли со счета {self.deposit} руб')
        else:
            print(f'Не удалось снять {self.deposit} рублей')
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        self.balance += self.withdraw
        print(f'Вы пополнили счет на {self.withdraw} руб')
    def account(self):
        print("Номер счета: "+self.acc_numb,"Баланс: "+str(self.balance))
user = Bank(random.randint(0,100000000),(str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])+str(azb[random.randint(0,len(azb)-1)])))
while a != 'Стоп':
    a = input()
    if a == 'пополнение':
        b = int(input('Сумма пополнения :'))
        user.withdraw(b)
    elif a == 'снятие':
        b = int(input('Сумма снятия :'))
        user.deposit(b)
    elif a == 'Данные':
        for i in range(3):
            n =input('Введите пароль :')
            if n == '7592':
                user.account()
                break
            else:
                print('Неверный пароль!')
                i += 1
                if i == 3:
                    print("Доступ к аккаунту заблокирован")
                    a= 'Стоп'



