tuplex = [(4, 6, 2, 8, 3, 1)]
list = []
for element in tuplex:
    for index in element:
        list.append(index)

list.append(int(input("Enter a number: ")))
del tuplex
tuplex = tuple(list)
print(tuplex)