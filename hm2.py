class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Транспортное средство заводится")
        
    def stop(self):
        print("Транспортное средство останавливается")
        
    def info(self):
        print(f"Брэнд - {self.brand},\nМодель - {self.model},\nГод - {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        
    def start(self):
        print("Машина заводится")
        
    def stop(self):
        print("Машина останавливается")
        
    def open_trunk(self):
        print("Багажник открыт")
        
    def info(self):
        print(f"Брэнд - {self.brand},\nМодель - {self.model},\nГод - {self.year},\nКоличество дверей: {self.doors}")
    
car = Car("Тойота", "Камри", 2017, 4)
car.open_trunk()
car.info()
car.start()
car.stop()

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_of_bicycle):
        super().__init__(brand, model, year)
        self.type_of_bicycle = type_of_bicycle
        
    def start(self):
        print("Велосипед начинает движение")
        
    def stop(self):
        print("Велосипед останавливается")
        
    def ring_bell(self):
        print("Звонок звенит")
        
    def info(self):
        print(f"Брэнд - {self.brand},\nМодель - {self.model},\nГод - {self.year},\nТип велосипеда - {self.type_of_bicycle}")
        

bicycle = Bicycle("Трэк", "Марлин 7", 2022, "Горный")
bicycle.ring_bell()
bicycle.info()
bicycle.start()
bicycle.stop()


class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length = length
        
    def start(self):
        print("Лодка отплывает")
        
    def stop(self):
        print("Лодка причаливает")
        
    def anchor(self):
        print("Якорь спущен")
        
    def info(self):
        print(f"Брэнд - {self.brand},\nМодель - {self.model},\nГод - {self.year},\nДлина лодки - {self.length} метров")

boat = Boat("Йамаха", "242X", 2021, 7.5)
boat.anchor()
boat.info()
boat.start()
boat.stop()



#classroom hm
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")

class Walker:
    def walk(self):
        print(f"{self.name} ходит")

class Swimmer:
    def swim(self):
        print(f"{self.name} плавает")

class Flyer:
    def fly(self):
        print(f"{self.name} летает")

class Penguin(Animal, Walker, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить и плавать")
        
penguin = Penguin("Пингвин")
penguin.describe()
penguin.walk()
penguin.swim()
penguin.eat()
penguin.sleep()


class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить, плавать и летать")
        
duck = Duck("Утка")
duck.describe()
duck.walk()
duck.swim()
duck.fly()
duck.eat()
duck.sleep()

class Bat(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может летать")

bat = Bat("Летучая мышь")
bat.describe()
bat.fly()
bat.eat()
bat.sleep()


