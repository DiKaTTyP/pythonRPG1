import random
Class = ["А","Б","В","Г"]
Name = ["Вася","Петя","Александр","Мария","Екатерина","Димон","Сеня","Аркаша","Петр Васильевич","Николь"]
First_name = ["Иванов","Петров","Сидоров","Меринов","Васильев"]
class Child():
    def __init__(self,name,first_name,number_class):
        self.name = name
        self.first_name = first_name
        self.number_class = number_class
    def id(self):
        print(self.name,self.first_name,self.number_class)
child_class = str(random.randint(0,11))+Class[random.randint(0,len(Class)-1)]
child = Child(Name[random.randint(0,len(Name)-1)],First_name[random.randint(0,len(First_name)-1)],child_class)
child.id()