password = []
for num in range(3, 21):
    for i in range(1, 20):
        for j in range(2, 20):
            if num % (i + j) == 0 and i != j and j > i:
                password.append(i)
                password.append(j)
            else:
                continue
    print(f"{num} - " + ' '.join(map(str, password)))
    password.clear()