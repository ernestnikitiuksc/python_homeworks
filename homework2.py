'''Задание 1**

Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России. Считайте, что список geo_logs легко помещается в оперативной памяти.
'''
geo_logs = [

    {'visit1': ['Москва', 'Россия']},
    
    {'visit2': ['Дели', 'Индия']},
    
    {'visit3': ['Владимир', 'Россия']},
    
    {'visit4': ['Лиссабон', 'Португалия']},
    
    {'visit5': ['Париж', 'Франция']},
    
    {'visit6': ['Лиссабон', 'Португалия']},
    
    {'visit7': ['Тула', 'Россия']},
    
    {'visit8': ['Тула', 'Россия']},
    
    {'visit9': ['Курск', 'Россия']},
    
    {'visit10': ['Архангельск', 'Россия']},
    
]

for i in range(0, len(geo_logs)):
    for key in geo_logs[i].values():
        if  'Россия' in key:
            print(geo_logs[i])



'''**Задание 2**
Выведите на экран все уникальные гео-ID из значений словаря ids. Т. е. список вида [213, 15, 54, 119, 98, 35]
'''

ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

array =[]
for key in ids.values():
    array = array + key
print(sorted(set(array), reverse = True))



# **Задание 3**
# Список поисковых запросов. Получить распределение количества слов в них. Т. е. поисковых запросов из одного слова 5%, из двух - 7%, из трех - 3% итд.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]


num_of_words_array = []

for i in range(0, len(queries)):
    num_of_words_array.append(len(queries[i].split(' ')))

max_number_in_array = max(num_of_words_array)

for i in range(1, max_number_in_array+1):
    print(f"количество слов - {i:d} встречается в  {num_of_words_array.count(i)/len(num_of_words_array)*100:.2f} %" )


# **Задание 4**
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т. е. в данном примере скрипт должен возвращать 'yandex'.


stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98}

maximum = max(stats, key=stats.get)
print(maximum, stats[maximum])



# **Задание 5**

# Дан поток логов по количеству просмотренных страниц для каждого пользователя. 
# Список отсортирован по ID пользователя. Вам необходимо написать алгоритм, который 
# считает среднее значение просмотров на пользователя. Т. е. надо посчитать отношение 
# суммы всех просмотров к количеству уникальных пользователей. Учтите, что весь список 
# stream не помещается в оперативную память, т. е. его нужно обрабатывать поэлементно в цикле.

stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',    
    '2018-05-03,user4,9',
    '2018-05-11,user4,11'
]

num_of_words_array = []

for i in range(0, len(stream)):
    num_of_words_array.append(stream[i].split(','))

#Количество всех просмотров
sumOfWholeViews = sum([int(x[2]) for x in num_of_words_array])

#Количество уникальных юзеров
uniqueUsers = len(set([x[1] for x in num_of_words_array]))

print(sumOfWholeViews/uniqueUsers)



# **Задание 6**
# Дана статистика рекламных кампаний по дням. Напишите алгоритм, 
# который по паре дата-кампания ищет значение численного столбца. 
# Т. е. для даты '2018-01-01' и 'google' нужно получить число 25. 
# Считайте, что все комбинации дата-кампания уникальны, а список 
# stats легко помещается в оперативной памяти.

stats = [
    ['2018-01-01', 'google', 25],
    ['2018-01-01', 'yandex', 65],
    ['2018-01-01', 'market', 89],
    ['2018-01-02', 'google', 574],
    ['2018-01-02', 'yandex', 249],
    ['2018-01-02', 'market', 994],
    ['2018-01-03', 'google', 1843],
    ['2018-01-03', 'yandex', 1327],  
    ['2018-01-03', 'market', 1764],    
]


companyPresent = False
datePresent = False

print("enter date format year-month-day")
date = input()
print("enter company")
company = input()

for i in range(0, len(stats)):
    if date in stats[i]:
        datePresent = True

for i in range(0, len(stats)):
    if company in stats[i]:
        companyPresent = True

if companyPresent == True and datePresent == True:
    print([x[2] for x in stats if x[0] == date and x[1] == company])
else:
    print("no data for entered company or date, please check format and try again")