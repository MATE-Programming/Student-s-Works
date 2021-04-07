#PROBLEM 1
a = [10,20,30,20,10,50,60,40,80,50,40]
newList = []
for x in a:
    if (newList.count(x)!=0):
        pass
    else:
        newList.append(x)
print(newList)

#problem 2
"""a = [7,16,43,27,49,97,81]
flag = True
for x in a:
    for num in range (2, x//2+1):
        if (x % num == 0):
            flag=False
            break
    if flag:
        print(x, ' - простое число')
    else:
        print(x, ' - не простое число')

"""


#PROBLEM 3
'''a= [1,2,3,4,5,6,7,8,9]
even = []
odd = []
for x in a:
    if x % 2 == 0:
        even.append(x)
print(sum(even))
for i in a:
        if i % 2 != 0:
            odd.append(i)
print(sum(odd))


b = [2,4,6,8,10,12,14,16,18,20]
even =[]
odd = []
for x in b:
    if x % 2 == 0:
        even.append(x)
print(sum(even))
for i in b:
        if i % 2 != 0:
            odd.append(i)
print(sum(odd))
'''


#problem 4
s = ['abc', 'aba', 'xyz', '1221']
ll = []
for q in s:
    if len(q) >= 2:
        ll.append(q)
        if q[0] == q[-1]:
            ll.append(q)
print(ll.count(q))

ss = ['oxxo', '123', 'h&m']
ls = []
for r in ss:
    if len(r) >= 2:
        ls.append(r)
        if r[0] == r[-1]:
            ls.append(r)
print(ls.count(r))


#problem 5
"""p = [20,89,33,1,2,5,61,55]
print("Largest number is ",max(p))
p.sort()
print("Second largest number is ", p[-2])"""


