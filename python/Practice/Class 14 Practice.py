class Animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    
    def do_sound(self):
        print("I don't know how to sound\n\n")

    def __str__(self):
        return self.name

animal=Animal("Meaw", 2, "Black")
print("Name from Animal Class: ",animal.name)
print("Age from Animal Class: ",animal.age)
print("Color from Animal Class: ",animal.color)
animal.do_sound()


class Cat(Animal):
    def __init__(self, name, age, color,is_lazy):
        super().__init__(name, age, color) #those values are already inherited from Animal Class
        self.is_lazy=is_lazy

    def do_sound(self):
        print("Meow\n\n")

    def __len__(self):
        return int(self.age)

class Dog(Animal):
    def do_sound(self):
        print("Gheu")
    
    def guard_the_house(self):
        print(f"{self.name} is guarding the house\n\n")


mini=Cat("Mini", 1.5,"Pink" , True)
print("Name from Cat Class: ",mini.name)
print("Age from Cat Class: ",mini.age)
print("Color from Cat Class: ",mini.color)
mini.do_sound()


tommy=Dog("Tommy", 2.5, "Brown")
print("Name from Dog Class: ",tommy.name)
print("Age from Dog Class: ",tommy.age)
print("Color from Dog Class: ",tommy.color)
tommy.do_sound()
tommy.guard_the_house()


cow=Animal("Lali", 3.5, "Red")
cow.do_sound()
print(cow)
print(len(mini))
