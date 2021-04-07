# problem3
l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d'), (), ()]
for i in l:
    if i:
        c = []
        c += [i]
        print(c, end=' ')