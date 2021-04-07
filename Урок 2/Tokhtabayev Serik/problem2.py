# problem2
i = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
for x in i:
    a = list(x)
    a.pop(-1)
    a.append(100)
    a = tuple(a)
    print(a, end=" ")
