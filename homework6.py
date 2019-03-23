import pandas as pd

# **Задание 1**

# Используем файл keywords.csv.

# Необходимо написать гео-классификатор, который каждой строке сможет выставить 
# географическую принадлежность определенному региону. Т. е. если поисковый запрос 
# содержит название города региона, то в столбце 'region' пишется название этого 
# региона. Если поисковый запрос не содержит названия города, то ставим 'undefined'.

# Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

table = pd.read_csv('/Users/erik/Documents/NETOLOGY_DATA/Python1/Python6/keywords.csv')

geo_data = {

    'Центр': ['москва', 'тула', 'ярославль'],

    'Северо-Запад': ['петербург', 'псков', 'мурманск'],

    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']

}

def checkTrue(row):
    for geo, geo2 in geo_data.items():
        for i in range(len(row["keyword"].split(" "))):
            var = "undefined"
            if row["keyword"].split(" ")[i] in geo2:
                var = geo
                return var
            return var


table["region"] = table.apply(checkTrue, axis = 1)

print(table.sort_values('region', ascending=True).tail(50))


# **Задание 2**

# Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
#     - оценка 2 и меньше - низкий рейтинг
#     - оценка 4 и меньше - средний рейтинг
#     - оценка 4.5 и 5 - высокий рейтинг

# Результат классификации запишите в столбец class

import pandas as pd

ratings = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python6/ml-latest-small/ratings.csv")

def rateClass(row):
    if row.rating <= 2:
        return "низкий рейтинг"
    if row.rating > 2 and row.rating <=4:
        return "средний рейтинг"
    if row.rating > 4:
        return "высокий рейтинг"



ratings["class"] = ratings.apply(rateClass, axis = 1)

print(

ratings.head()

)


# **Задание 3**

# Посчитайте среднее значение Lifetime киноманов (пользователи,
# которые поставили 100 и более рейтингов). Под Lifetime понимается
# разница между максимальным и минимальным значением timestamp для
# каждого пользователя. Ответ дайте в днях.

import pandas as pd
from datetime import datetime

ratings = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python6/ml-latest-small/ratings.csv")

ratings_filtered = ratings.groupby("userId").count()

ratings_filtered = ratings_filtered[ratings_filtered.rating > 100]
ratings_filtered = ratings_filtered.reset_index()

ratings = ratings[ratings.userId.isin (ratings_filtered.userId.tolist())]

ratings = ratings.groupby('userId').agg({'timestamp': ['min', 'max']}).reset_index()

ratings["lifetime"] = ratings["timestamp"]["max"] - ratings["timestamp"]["min"]

average_lifetime = sum(ratings["lifetime"]) / len(ratings.userId)

endDate = datetime.fromtimestamp(average_lifetime)
startDate = datetime.fromtimestamp(0)

period =  endDate - startDate

num_of_days = period.days

print(
"average lifetime is {} days".format (num_of_days),
)


# **Задание 4**

# Есть мнение, что "раньше снимали настоящее кино, не то что сейчас". Ваша задача 
# проверить это утверждение, используя файлы с рейтингами фильмов из материалов 
# занятия. Т. е. проверить верно ли, что с ростом года выпуска фильма его средний 
# рейтинг становится ниже.

# При этом мы не будем затрагивать субьективные факторы выставления этих рейтингов, 
# а пройдемся по следующему алгоритму:

# 1. В переменную years запишите список из всех годов с 1950 по 2010.

# 2. Напишите функцию production_year, которая каждой строке из названия фильма 
#     выставляет год выпуска. Не все названия фильмов содержат год выпуска в одинаковом 
#     формате, поэтому используйте следующий алгоритм:

#     - для каждой строки пройдите по всем годам списка years
#     - если номер года присутствует в названии фильма, то функция возвращает этот год как год выпуска
#     - если ни один из номеров года списка years не встретился в названии фильма, то возвращается 1900 год

# 3. Запишите год выпуска фильма по алгоритму пункта 2 в новый столбец 'year'

# 4. Посчитайте средний рейтинг всех фильмов для каждого значения столбца 'year' и 
# отсортируйте результат по убыванию рейтинга


import pandas as pd

ratings = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python6/ml-latest-small/ratings.csv")
movies = pd.read_csv("/Users/erik/Documents/NETOLOGY_DATA/Python1/Python6/ml-latest-small/movies.csv")

years = list(range(1950,2011))

def setYear(row):
    year = 1900
    for i in years:
        if str(i) in (row["title"]):
            year = str(i)
    return year
            
movies["year"] = movies.apply(setYear, axis = 1)

ratings = ratings.groupby('movieId').agg({'rating': ["mean"]}).reset_index()
ratings.columns = ratings.columns.droplevel(1)

joined = movies.merge(ratings, on='movieId')

joined = joined.groupby('year').agg({'rating': ["mean"]})

print(joined)
