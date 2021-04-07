data = open('DATA.txt', 'w', encoding='utf-8')
data.write('ytdf,gyugyguyg ,utuyfgygh')
data.close()
i = 0
data = open('DATA.txt', encoding='utf-8')
for x in data:
    for z in range(len(x) - 1):
        if x[z] == ' ' and x[z + 1] != ' ':
            i+=1
        if x[z] == '-' and x[z + 1] == ' ':
            i -= 1
        if x[z] == ',':
            i += 1
        if x[z] == ',' and x[z + 1] == ' ':
            i -=1
        if x[z] == ' ' and x[z + 1] == ',':
            i -= 1
print(i + 1)