L = [(), (), (‘’,), (‘a’, ‘b’), (‘a’, ‘b’, ‘c’), (‘d’)]
a = list[L]
a.remove('()')
a.remove('()')
print(tuple(a))
