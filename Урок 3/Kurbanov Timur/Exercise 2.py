set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 20, 10}
sum = 0

set1 = set1 & set2

for element in set1:
    sum += element

print(sum)