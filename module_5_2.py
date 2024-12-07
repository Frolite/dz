class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor


    def go_to(self, new_floor: int)->int:
        if new_floor <= self.number_of_floor:
            i = 1
            while i <= new_floor:
                print(i)
                i+=1

        else:
            print("Такого этажа не существует.")


    def __len__(self):
        return self.number_of_floor
    

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1) # __str__
print(h2)

h1.go_to(5)
h2.go_to(10)

print(len(h1)) # __len__
print(len(h2))
