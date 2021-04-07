nums = (1,2,3)
cache = []
number = 0

for element in reversed(nums):
    cache.append(element)

for element in range(0, len(cache)):
    if element == 0:
        number += cache[element]
    elif element > 0:
        number += cache[element] * 10 ** element

print(number)