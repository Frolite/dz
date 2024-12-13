class House:
    def __init__(self, name, floors):
        self.name = name  # Название дома
        self.floors = floors  # Количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # False

h1 = h1 + 10  # Увеличение этажей на 10
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # Увеличение этажей на 10 с помощью +=
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # Увеличение этажей на 10 с помощью radd
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False
