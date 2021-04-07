per = open('photo_2021-02-02_16-21-40.jpg', 'rb')
per1 = open('img.png', 'wb')
for x in per:
    per1.write(x)
