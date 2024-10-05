my_dick = {"Egor":2007, "Slava":1488}
print(my_dick)
print(my_dick["Egor"])
print(my_dick.get("Vetal"))
my_dick.update({"Max": 2020,
		"Den": 2000})
a = my_dick.pop("Slava")
print(a)
print(my_dick)

my_set = {1, 2, 1 ,3 ,3 ,True , 'a', 'a', 'c'}
print(my_set)
my_set.update([5, 6], 'd')
my_set.discard(1)
print(my_set)