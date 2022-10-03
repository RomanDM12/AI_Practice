# AI_Practice

1.3.1 Задание
Создать 8x8 матрицу и заполнить её в шахматном порядке нулями и единицами.

import numpy as np
m = np.zeros([8,8])
m[::2, ::2] = 1
m[1::2, 1::2] = 1
print(m)

1.3.2 Задание
Создать 5x5 матрицу со значениями в строках от 0 до 4. Для создания необходимо использовать функцию arange.

m = np.zeros([5,5])
m += np.arange(5)
print(m)

1.3.3 Задание
Создать массив 3x3x3 со случайными значениями

a = np.random.random((3, 3, 3))
print(a)

1.3.4 Задание
Создать матрицу с 0 внутри, и 1 на границах.

m = np.ones([5,5])
m[1:-1, 1:-1] = 0
print(m)

1.3.5 Задание
Создайте массив и отсортируйте его по убыванию.

a = np.array([1,4,5,2,6,8,9,5,6,7,0,3])
b = np.sort(a)
lEn = np.size(b)
for i in range(lEn - 1, 0, -1):
    print(b[i])

1.3.6 Задание
Создайте матрицу, выведите ее форму, размер и размерность.

a = np.array([[9, 8, 7, 5], [4, 1, 3, 2]])
print(a.shape)
print(a.size)
print(a.size * a.itemsize)

2.3.1 Задание
Найдите евклидово расстояние между двумя Series (точками) a и b, не используя встроенную формулу.

a = pd.Series([5, 8, 3, 4])
b = pd.Series([2, 4, 6, 7])
sum((a - b)**2)**.5

2.3.2 Задание
Найдите в Интернете ссылку на любой csv файл и сформируйте из него фрейм данных (например, коллекцию фреймов данных можно найти здесь: https://github.com/akmand/datasets).

import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/airlines.csv'

dataframe = pd.read_csv(url)

2.3.3 Задание
Проделайте с получившемся из предыдущего задания фреймом данных те же действия, что и в примерах 2.2.5-2.2.7.

print(dataframe.head(3))
print(dataframe.tail(3))
print(dataframe.shape)
print(dataframe.describe())

print(dataframe.iloc[1:5])

print(dataframe[dataframe['Time'] == '15'].head(2))

