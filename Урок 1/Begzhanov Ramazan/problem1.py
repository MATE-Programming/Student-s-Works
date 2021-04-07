a = [10,20,30,20,10,50,60,40,80,50,40]
b = list(set(a))
b.sort()
b.remove(40)
b.insert(5, 40)
print(b)
