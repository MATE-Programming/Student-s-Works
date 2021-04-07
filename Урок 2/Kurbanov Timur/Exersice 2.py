tuplex = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list = []
cache = []

for element in range(0, len(tuplex) - 1):
    list.append(tuplex[element])

for element in range(len(tuplex) - 1, len(tuplex)):
    for index in tuplex[element]:
        cache.append(index)

cache[-1] = int(input("Enter a number: "))

cache = tuple(cache)

list.append(cache)
del cache
del tuplex

tuplex = list
del list

print(tuplex)

