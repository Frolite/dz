immutable_var = True, "строка", 5
print(immutable_var)

#immutable_var[0] = False
#print(immutable_var)

#TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, True, "string"]
mutable_list[0] = 2
mutable_list.append(False)
print(mutable_list)