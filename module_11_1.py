#запрос элемента Яндекс карты
from requests import get, ConnectionError

params = {"ll": "37.677751,55.757718",  #координаты для запроса в Static API
          "spn": "0.016457,0.00619",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params) #запрос на получение данных
    print(response)
except ConnectionError:     #вызов исключения
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:   #запись полученных данный в новый файл (получение части запрошенной карты)
        file.write(response.content)

#работа с массивом данных
import numpy as np

a = np.array([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
print(a.sum())        # сумма всех чисел массива
print()
print(a.min())        # минимальный элемент массива
print()
print(a.max())        # максимсальный элемент массива
print()
print(a.sum(axis=0))  # сумма чисел в каждом столбце
print()
print(a.sum(axis=1))  # сумма чисел в каждой строке
print()
print(a.min(axis=0))  # минимум по столбцам
print()
print(a.max(axis=1))  # максимум по строкам

#работа с изображением
from PIL  import Image
image = Image.open("delfini.jpeg")
cropped = image.crop((0, 80, 200 ,400))
cropped.save('/Users/ekaterina/PythonProject/pythonProject/Potok/delfini_1.jpeg')
image_1 = Image.open("delfini_1.jpeg")


