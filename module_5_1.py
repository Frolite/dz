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
            

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)