# Problem1
tuplex = [(4, 6, 2, 8, 3, 1)]
txt = int(input())
for i in tuplex:
    a = list(i)
    a.append(txt)
    a = tuple(a)
print(a)


