my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while my_list[num] >= 0 and num != len(my_list) + 1:
	if my_list[num] != 0:
		print(my_list[num])
	num += 1