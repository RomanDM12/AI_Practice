{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "55c28191",
   "metadata": {},
   "source": [
    "### 1.3.1 Задание\n",
    "Создать 8x8 матрицу и заполнить её в шахматном порядке нулями и\n",
    "единицами."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "e3cf4976",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 0. 1. 0. 1. 0. 1. 0.]\n",
      " [0. 1. 0. 1. 0. 1. 0. 1.]\n",
      " [1. 0. 1. 0. 1. 0. 1. 0.]\n",
      " [0. 1. 0. 1. 0. 1. 0. 1.]\n",
      " [1. 0. 1. 0. 1. 0. 1. 0.]\n",
      " [0. 1. 0. 1. 0. 1. 0. 1.]\n",
      " [1. 0. 1. 0. 1. 0. 1. 0.]\n",
      " [0. 1. 0. 1. 0. 1. 0. 1.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "m = np.zeros([8,8])\n",
    "m[::2, ::2] = 1\n",
    "m[1::2, 1::2] = 1\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0625cb6",
   "metadata": {},
   "source": [
    "### 1.3.2 Задание\n",
    "Создать 5x5 матрицу со значениями в строках от 0 до 4. Для создания\n",
    "необходимо использовать функцию arange."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1c66f80e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 1. 2. 3. 4.]\n",
      " [0. 1. 2. 3. 4.]\n",
      " [0. 1. 2. 3. 4.]\n",
      " [0. 1. 2. 3. 4.]\n",
      " [0. 1. 2. 3. 4.]]\n"
     ]
    }
   ],
   "source": [
    "m = np.zeros([5,5])\n",
    "m += np.arange(5)\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6006139",
   "metadata": {},
   "source": [
    "### 1.3.3 Задание\n",
    "Создать массив 3x3x3 со случайными значениями"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "36d00d4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[0.02645347 0.66663459 0.35681466]\n",
      "  [0.80333814 0.43278857 0.35837797]\n",
      "  [0.42901806 0.80719174 0.70504727]]\n",
      "\n",
      " [[0.77199511 0.44465569 0.05516203]\n",
      "  [0.2616669  0.95323847 0.58668133]\n",
      "  [0.80041557 0.19412251 0.23629579]]\n",
      "\n",
      " [[0.68861499 0.85559182 0.22347147]\n",
      "  [0.32900914 0.19823229 0.93054833]\n",
      "  [0.88789858 0.75252697 0.67862906]]]\n"
     ]
    }
   ],
   "source": [
    "a = np.random.random((3, 3, 3))\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fa4b8181",
   "metadata": {},
   "source": [
    "### 1.3.4 Задание\n",
    "Создать матрицу с 0 внутри, и 1 на границах."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "f7569411",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 1. 1. 1.]\n",
      " [1. 0. 0. 0. 1.]\n",
      " [1. 0. 0. 0. 1.]\n",
      " [1. 0. 0. 0. 1.]\n",
      " [1. 1. 1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "m = np.ones([5,5])\n",
    "m[1:-1, 1:-1] = 0\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3363b353",
   "metadata": {},
   "source": [
    "### 1.3.5 Задание\n",
    "Создайте массив и отсортируйте его по убыванию."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "810cbad9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "6\n",
      "5\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,4,5,2,6,8,9,5,6,7,0,3])\n",
    "b = np.sort(a)\n",
    "lEn = np.size(b)\n",
    "for i in range(lEn - 1, 0, -1):\n",
    "    print(b[i])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3768d233",
   "metadata": {},
   "source": [
    "#### 1.3.6 Задание\n",
    "Создайте матрицу, выведите ее форму, размер и размерность."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "47b8d40d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 4)\n",
      "8\n",
      "64\n"
     ]
    }
   ],
   "source": [
    "a = np.array([[9, 8, 7, 5], [4, 1, 3, 2]])\n",
    "print(a.shape)\n",
    "print(a.size)\n",
    "print(a.size * a.itemsize)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "757bdb10",
   "metadata": {},
   "source": [
    "### 2.3.1 Задание\n",
    "Найдите евклидово расстояние между двумя Series (точками) a и b, не\n",
    "используя встроенную формулу."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "e9363e3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.557438524302"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = pd.Series([5, 8, 3, 4])\n",
    "b = pd.Series([2, 4, 6, 7])\n",
    "sum((a - b)**2)**.5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f5398ca",
   "metadata": {},
   "source": [
    "### 2.3.2 Задание\n",
    "Найдите в Интернете ссылку на любой csv файл и сформируйте из него\n",
    "фрейм данных (например, коллекцию фреймов данных можно найти\n",
    "здесь: https://github.com/akmand/datasets)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "abb6fe44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Flight</th>\n",
       "      <th>AirportFrom</th>\n",
       "      <th>AirportTo</th>\n",
       "      <th>DayOfWeek</th>\n",
       "      <th>Time</th>\n",
       "      <th>Length</th>\n",
       "      <th>Delay</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>CO</td>\n",
       "      <td>269</td>\n",
       "      <td>SFO</td>\n",
       "      <td>IAH</td>\n",
       "      <td>3</td>\n",
       "      <td>15</td>\n",
       "      <td>205</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>US</td>\n",
       "      <td>1558</td>\n",
       "      <td>PHX</td>\n",
       "      <td>CLT</td>\n",
       "      <td>3</td>\n",
       "      <td>15</td>\n",
       "      <td>222</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AA</td>\n",
       "      <td>2400</td>\n",
       "      <td>LAX</td>\n",
       "      <td>DFW</td>\n",
       "      <td>3</td>\n",
       "      <td>20</td>\n",
       "      <td>165</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Airline  Flight AirportFrom AirportTo  DayOfWeek  Time  Length  Delay\n",
       "0      CO     269         SFO       IAH          3    15     205      1\n",
       "1      US    1558         PHX       CLT          3    15     222      1\n",
       "2      AA    2400         LAX       DFW          3    20     165      1"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "url = 'https://raw.githubusercontent.com/akmand/datasets/main/airlines.csv'\n",
    "\n",
    "dataframe = pd.read_csv(url)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9861707",
   "metadata": {},
   "source": [
    "### 2.3.3 Задание\n",
    "Проделайте с получившемся из предыдущего задания фреймом данных\n",
    "те же действия, что и в примерах 2.2.5-2.2.7."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "cec87f70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Airline  Flight AirportFrom AirportTo  DayOfWeek  Time  Length  Delay\n",
      "0      CO     269         SFO       IAH          3    15     205      1\n",
      "1      US    1558         PHX       CLT          3    15     222      1\n",
      "2      AA    2400         LAX       DFW          3    20     165      1\n",
      "       Airline  Flight AirportFrom AirportTo  DayOfWeek  Time  Length  Delay\n",
      "539380      FL     609         SFO       MKE          5  1439     255      0\n",
      "539381      UA      78         HNL       SFO          5  1439     313      1\n",
      "539382      US    1442         LAX       PHL          5  1439     301      1\n",
      "(539383, 8)\n",
      "              Flight      DayOfWeek           Time         Length  \\\n",
      "count  539383.000000  539383.000000  539383.000000  539383.000000   \n",
      "mean     2427.928630       3.929668     802.728963     132.202007   \n",
      "std      2067.429837       1.914664     278.045911      70.117016   \n",
      "min         1.000000       1.000000      10.000000       0.000000   \n",
      "25%       712.000000       2.000000     565.000000      81.000000   \n",
      "50%      1809.000000       4.000000     795.000000     115.000000   \n",
      "75%      3745.000000       5.000000    1035.000000     162.000000   \n",
      "max      7814.000000       7.000000    1439.000000     655.000000   \n",
      "\n",
      "               Delay  \n",
      "count  539383.000000  \n",
      "mean        0.445442  \n",
      "std         0.497015  \n",
      "min         0.000000  \n",
      "25%         0.000000  \n",
      "50%         0.000000  \n",
      "75%         1.000000  \n",
      "max         1.000000  \n",
      "  Airline  Flight AirportFrom AirportTo  DayOfWeek  Time  Length  Delay\n",
      "1      US    1558         PHX       CLT          3    15     222      1\n",
      "2      AA    2400         LAX       DFW          3    20     165      1\n",
      "3      AA    2466         SFO       DFW          3    20     195      1\n",
      "4      AS     108         ANC       SEA          3    30     202      0\n",
      "Empty DataFrame\n",
      "Columns: [Airline, Flight, AirportFrom, AirportTo, DayOfWeek, Time, Length, Delay]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "print(dataframe.head(3))\n",
    "print(dataframe.tail(3))\n",
    "print(dataframe.shape)\n",
    "print(dataframe.describe())\n",
    "\n",
    "print(dataframe.iloc[1:5])\n",
    "\n",
    "print(dataframe[dataframe['Time'] == '15'].head(2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd5fdafc",
   "metadata": {},
   "source": [
    "### 3.3.2\n",
    "Загрузить фрейм данных по ссылке:\n",
    "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv.\n",
    "Необходимо выполнить нормализацию первого числового признака\n",
    "(sepal_length_cm) с использованием минимаксного преобразования, а\n",
    "второго (sepal_width_cm) с задействованием z-масштабирования."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3892362a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
