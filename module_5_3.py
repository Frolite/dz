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


    def __eq__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor == other.number_of_floor
        else:
            return None

    def __lt__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor < other.number_of_floor
        else:
            return None

    def __le__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor <= other.number_of_floor
        else:
            return None

    def __gt__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor > other.number_of_floor
        else:
            return None

    def __ge__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor >= other.number_of_floor
        else:
            return None


    def __ne__(self, other):
        if isinstance(other, int) == True and isinstance(other, House) == True:
            return self.number_of_floor != other.number_of_floor
        else:
            return None


    def __add__(self, value):
        if isinstance(value, int) == True:
            return self.number_of_floor + value
        else:
            return None

    def __radd__(self, value):
        if isinstance(value, int) == True:
            return self.number_of_floor + value
        else:
            return None

    def __iadd__(self, value):
        if isinstance(value, int) == True:
            return self.number_of_floor + value
        else:
            return None

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

h1.go_to(5)
h2.go_to(10)

print(len(h1)) # __len__
print(len(h2)) 

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__