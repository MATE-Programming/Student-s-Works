data_read = open('DATA.txt', mode='r', encoding='UTF-8')
data_write = open('количество слов в DATA.txt', mode='w', encoding='UTF-8')

sum = 0

for element in data_read:
    print(element)
    for words in element:
        if words == ' ' or words == ',':
            sum += 1

data_write.write(str(sum))