import pandas as pd
import numpy as np
from numpy import linalg

# **Задание 1**
# ​
# Создайте numpy array с элементами от числа N до 0
# (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

def make_numpy_array(n):
    x = np.arange(n-1, -1 , -1)
    return x

print(make_numpy_array(20))


# **Задание 2**
# ​
# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.

def make_diag_matrix_and_count_values(n):
    x = np.diag(np.arange(n-1, -1 , -1), k=0)
    print(x)

    sum = 0
    for i in range(n):
        sum += x[i][i]


    print("sum of diagonal elements = {}".format(sum))

make_diag_matrix_and_count_values(20)


# **Задание 3**
# ​
# Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. 
# Определите какому фильму было выставлено больше всего оценок 5.0.

data1 = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python5/ml-latest-small/ratings.csv")

data1 =data1[data1.rating == 5.0]
data1 = data1.groupby('movieId')['rating'].agg('count').reset_index(name = "counts")
print(
    data1.sort_values(by='counts', ascending = False).head(1)
)

data2 = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python5/ml-latest-small/movies.csv")

data2 = data2[data2.movieId == 318]["title"]
print(
    data2
)

# в данном задании у меня не получилось красиво вывести информация
# я хотел вывести чтото вроде print("больше всего количество рейтинга 5.0 у {}".format(data2["title"]))
# Но так не получилось. Подскажите пожалуйста как в моем случае можно эту информацию вытащить как стринг?
#




# **Задание 4**
# ​
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) 
# категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.

data = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python5/power.csv")


filtered_countries1 = data[ (data['country']=='Latvia') | (data['country']=='Estonia') | (data['country']=='Lithuania')]

filtered_countries2 = filtered_countries1[(filtered_countries1["category"] == 4) | (filtered_countries1["category"] == 12) | (filtered_countries1["category"] == 21) ]

filtered_countries3 = filtered_countries2[(filtered_countries2["year"] >= 2005) & (filtered_countries2["year"] <=2010)]

filtered_countries4 = filtered_countries3[(filtered_countries3["quantity"] >=0)]

print(
    filtered_countries4["quantity"].sum()
)



# **Задание 5**
# ​
# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3

a = np.array([[4,2,1], [1,3,0], [0,5,4]])
b = np.array([4,12,-3])

print(linalg.solve(a, b))

print(np.allclose( np.dot(a, linalg.solve(a, b)), b ))



