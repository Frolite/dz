import os
os.system("cls")
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f"Поездка на этаж {new_floor}")
        else:
            print("Такого этажа не существует")
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
del h1