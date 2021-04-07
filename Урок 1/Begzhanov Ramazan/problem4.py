a = ['abc','aba','xyz','1221']
b=[]
for x in a:
    if len(x) >= 2:
        b.append(x)
    if x[0]==x[-1]:
        b.append(x)
print(b.count(x))



a = ['oxxo', '123', 'h & m']
b=[]
for x in a:
    if len(x)>=2:
        b.append(x)
    if x[0]==x[-1]:
        b.append(x)
print(b.count(x))
