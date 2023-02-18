import random
c = ["Вася","Петя","Рекс","Шарик","Сем","Тор","Цезарь","Джек","Топа"]
ag= [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

class Dog(): #создвем класс собака
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f'Собака {self.name.title()} создана')

    def golos(self): #Команда собаки "Голос"
        print(self.name.title() + ' гавкает')

    def sidet(self): #Команда собаки "сидеть"
        print(self.name.title() + ' садится')
# Создаются переменные, которые выбирают имена и возраст собак
b = random.randint(0,8)
h = random.randint(0,13)
d = random.randint(0,8)
f = random.randint(0,13)
dog1 = Dog(c[b],ag[h])
dog2 = Dog(c[d],ag[f])
# Выводится имена, возраст и что умеет делать собака
print(dog1.name,dog1.age , ' умеет "Голос" и "Сидеть"',dog2.name,dog2.age,' умеет "Голос" и "Сидеть"')
a = input()
#Сравнивается команда, которую вводит человек с теми, которые умеет делать собака
if a == 'Голос' or a == 'голос':
    dog1.golos()
    dog2.golos()
elif a == 'Сидеть' or a == 'сидеть':
    dog1.sidet()
    dog2.sidet()
else:
    print('Он этого не умеет')