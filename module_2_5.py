def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        in_matrix = []
        matrix.append(in_matrix)
        j = 0
        while j < m:
            j += 1
            in_matrix.append(value)
    return matrix

resalt1 = get_matrix(4, 5, 4)
print(resalt1)

'''
resalt1 = get_matrix(2, 2, 10)
resalt2 = get_matrix(3, 5, 42)
resalt3 = get_matrix(4, 2, 13)
print(resalt1)
print(resalt2)
print(resalt3)
'''
