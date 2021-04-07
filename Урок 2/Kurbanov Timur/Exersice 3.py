tuplex = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'), (), ()]


for element in reversed(tuplex):
    if element == ():
        tuplex.remove(element)

print(tuplex)

tuplex = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'), (), ()]

for element in reversed(tuplex):
    if len(element) == 0:
        tuplex.remove(element)

print(tuplex)

#TODO узнать почему остаётся пустой кортеж после удаления и как обнулить счётчик!

tuplex = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'), ()]

for element in tuplex:
    if len(element) == 0:
        tuplex.remove(element)

print(tuplex)

#TODO узнать почему остаётся пустой кортеж после удаления и как обнулить счётчик!

tuplex = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'), ()]

for element in tuplex:
    if element == ():
        tuplex.remove(element)

print(tuplex)