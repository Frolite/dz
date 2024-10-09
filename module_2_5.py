def get_matrix(n, m, value):
    matrix = []
    if m > 0 and value > 0:
        for i in range(0, n):
            in_matrix = []
            matrix.append(in_matrix)
            j = 0
            while j < m:
                j += 1
                in_matrix.append(value)
        return matrix
    else:
        return matrix
resalt1 = get_matrix(2, 2, 10)
resalt2 = get_matrix(3, 5, 42)
resalt3 = get_matrix(4, 2, 13)
resalt4 = get_matrix(2, 0, 10)
resalt5 = get_matrix(2, 2, 0)
print(resalt1)
print(resalt2)
print(resalt3)
print(resalt4)
print(resalt5)
