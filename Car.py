import random
Color = ["Синий","Красный","Желтый","Зеленый","Оранжевый","Фиолетовый","Серый","Белый","Черный","Голубой","Коричневый","Бежевый"]

class Car():
    count = 0
    def __init__(self,color):
        Car.count = Car.count + 1
        self.max_speed = '120 km/ч'
        self.color = color
    def get_count(self):
        print('Всего машин: '+ str(Car.count),' Максимальная скорость: '+self.max_speed,' Цвет:'+self.color)
for x in range (random.randint(1,1000)):
    car = Car(Color[random.randint(0,len(Color)-1)])
    car.get_count()
