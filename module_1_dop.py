grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
student={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
student=sorted(list(student))
book={student[0]:sum(grades[0])/len(grades[0]), 
	student[1]:sum(grades[1])/len(grades[1]),
	student[2]:sum(grades[2])/len(grades[2]),
	student[3]:sum(grades[3])/len(grades[3]),
	student[4]:sum(grades[4])/len(grades[4])}
print(book)

#student=sorted(list(student))
#grades=[sum(grades[0])/len(grades[0]), 
#	sum(grades[1])/len(grades[1]),
#	sum(grades[2])/len(grades[2]),
#	sum(grades[3])/len(grades[3]),
#	sum(grades[4])/len(grades[4]),]
#book=dist(zip(student, grades))
#print(book)