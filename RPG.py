import random
import time
Classs = ["Маг","Танк"]#,"Лучник","Целитель"]
Type= ["Огонь","Холод","Яд"]
atack = ''
gg = 0
class RPG():
    def __init__(self,name,Class):
        self.name = name
        self.Class = Class
        print(f"Персонаж {self.name} создан, класс: {self.Class}.Вывести данные о персонаже?")


class Mage(RPG):
    def __init__(self,name,Class,HP,DP,punch,atack_type,HP1,DP1,punch1,atack_type1,Class1,gg):
        self.gg = gg
        self.name = name
        self.Class = Class
        self.HP1 = HP
        self.DP1 = DP
        self.punch1 = punch
        self.atack_type1 = atack_type
        self.HP2 = HP1
        self.DP2 = DP1
        self.punch2 = punch1
        self.atack_type2 = atack_type1
        self.Class2 = Class1
    def info(self):
        print(self.name, self.Class, self.HP1, self.DP1, self.punch1, self.atack_type1)

    def Atack(self):
        if self.atack_type1 == 'Огонь':
            self.atack1 = self.punch1 + 4
        elif self.atack_type1 == 'Холод':
            self.atack1 = self.punch1 + 3
        else:
            self.atack1 = self.punch1 + 6
        if self.Class2 == "Маг":
            if self.atack_type2 == 'Огонь':
                self.atack2 = self.punch2 + 4
            elif self.atack_type2 == 'Холод':
                self.atack2 = self.punch2 + 3
            else:
                self.atack2 = self.punch2 + 6
            print(f"Ваш урон равен {self.atack2}")
        else:
            self.atack2 = self.punch2
            print(f"Ваш урон равен {self.atack2}")
    def Defence(self):
        print(self.HP1)
        if self.HP1 > (self.atack2 - self.DP1):
            self.HP1 = self.HP1 - (self.atack2 - self.DP1)
            print(f"Вам был нанесен урон {(self.atack2)-self.DP1}, ваше здоровье равно:{self.HP1}")
        else:
            print("Игра окончена.Ваш персонаж был убит и ограблен")
            self.HP1 = 0
            self.HP2 = 0
            self.gg=1

class Tank(RPG):
    def __init__(self,name,Class,HP,DP,punch,atack_type,HP1,DP1,punch1,atack_type1,Class1,gg):
        self.gg = gg
        self.name = name
        self.Class = Class
        self.HP2 = HP
        self.DP2 = DP
        self.punch2 = punch
        self.atack_type2 = atack_type
        self.HP1 = HP1
        self.DP1 = DP1
        self.punch1 = punch1
        self.atack_type1 = atack_type1
        self.Class1 = Class1
    def info(self):
        print(self.name,self.Class,self.HP2,self.DP2,self.punch2,self.atack_type2)

    def Atack(self):
        self.atack2 = self.punch2

        if self.Class1 == 'Маг':
            if self.atack_type1 == 'Огонь':
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == 'Холод':
                self.atack1 = self.punch1 + 3
            else:
                self.atack1 = self.punch1 + 6
            print(f"Ваш урон равен {self.atack1}")
        else:
            self.atack1 =self.punch1
            print(f"Ваш урон равен {self.atack1}")


    def Defence(self):
        print(self.HP2)
        if self.HP2 > (self.atack1 - self.DP2):
            self.HP2 = self.HP2 - (self.atack1 - self.DP2)
            print(f"Вам был нанесен урон {(self.atack1) - self.DP2}, ваше здоровье равно:{self.HP2}")
        else:
            self.HP1 = 0
            self.HP2 = 0
            print("Игра окончена.Ваш персонаж был убит и ограблен")
            self.gg=1


print("Игра против компьютера/ игра с игроком?")
a=input()
if a == '1':
    print("Введите имя персонажа: ")
    name = input()
    b= "Танк"#Classs[random.randint(0,len(Classs)-1)]
    p1 = RPG('Компьютер',b)
    if b=="Маг":
        HP1= random.randint(125,250)
        DP1 = random.randint(5,15)
        punch1 = random.randint(25,45)
        atack_type1 = Type[random.randint(0,len(Type)-1)]
        person1 = Mage('Компъютер', b, HP1, DP1, punch1, atack_type1)
#   elif b=="":

#    elif b=="":

    else:
        HP1= random.randint(225,400)
        DP1 = random.randint(10,25)
        punch1 = random.randint(15,25)
        atack_type1 = "Площадь"




    c= input()
    if c=="Маг":
        p2=RPG(name,c)
        HP2= random.randint(125,250)
        DP2 = random.randint(5,15)
        punch2 = random.randint(25,45)
        atack_type2 = Type[random.randint(0,len(Type)-1)]


#   elif b=="":

#    elif b=="":

    elif c == "Танк":
        p2 = RPG(name, c)
        HP2 = random.randint(225,400)
        DP2 = random.randint(10,25)
        punch2 = random.randint(15,25)
        atack_type2 = "Площадь"
        person2 = Tank(name, c, HP2, DP2, punch2, atack_type2)
    else:
        print("Такого класса не существует")
    if b == "Танк":
        person1 = Tank('Компъютер', b, HP1, DP1, punch1, atack_type1,HP2, DP2, punch2, atack_type2,c,gg)
    else:
        person1 = Mage('Компъютер', b, HP1, DP1, punch1, atack_type1, HP2, DP2, punch2, atack_type2, c,gg)
    if c == "Маг":
        person2 = Mage(name, c, HP2, DP2, punch2, atack_type2,HP1, DP1, punch1, atack_type1,b,gg)
    else:
        person2 = Tank(name, c, HP2, DP2, punch2, atack_type2, HP1, DP1, punch1, atack_type1, b,gg)
print(person1.HP1)
while person1.HP1 >0 and person2.HP2>0:
    time.sleep(1)
    person2.Atack()
    person2.Defence()
    person1.Atack()
    person1.Defence()
