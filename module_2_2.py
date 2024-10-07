first, second, third = map(int,input().split())
if(first == second == third):
	print("3")
elif(first == second and first != third):
	print("2")
elif(first != second and first == third):
	print("2")
elif(second == third and first != second):
	print("2")
else:
	print("0")