# Библиотека для работы с изображениями
from PIL import Image

# Открываем картинку
w211 = Image.open('w211.jpg')


w211.show()

# Сохраняем файл как w212
w211.save('w212.jpeg')

w211.close()
