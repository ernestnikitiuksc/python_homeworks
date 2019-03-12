# Задание 1
# Дан список вида:
# Напишите функцию, которая возвращает сумму элементов на диагонали. Т. е. 13+32+23+35.

data = [
[13, 25, 23, 34],
[45, 32, 44, 47],
[12, 33, 23, 95],
[13, 53, 34, 35],
]

sum1 = 0

def diagonalSum(data):
    global sum1
    for i in range(len(data)):
        sum1 += data[i][i]
    return(sum1)

print(diagonalSum(data))


# Задание 2
# Дан список чисел, часть из которых имеют строковый тип или содержат буквы.
# Напишите функцию, которая возвращает сумму квадратов элементов, которые могут
# быть числами.

dataConverted = []

data1 = [1, '5', 'abc', 20, '2']


def squareSum(data1):
    for i in data1:
        if type(i) == int:
            dataConverted.append(i)
        elif type(i) == str:
            if i.isdigit() == True:
                dataConverted.append(int(i))
    return sum([x**2 for x in dataConverted])

print(squareSum(data1))



# Задание 3
# Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным
# значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js

import requests

k = []
v = []

def getMaxValue():
    for key in getInfo():
        k. append(key)
        v.append(getInfo()[key]["Value"])
    return k[v.index(max(v))], max(v)

def getInfo():
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    return  r.json()['Valute']

print(getMaxValue())


# Задание 4
# Последнее упражнение с занятия
# Добавьте в класс еще один формат, который возвращает название валюты (например, ‘Евро’).
# Добавьте в класс параметр diff (со значениями True или False), который в случае значения 
# True в методах eur и usd будет возвращать не курс валюты, а изменение по сравнению в прошлым значением.

import requests

class Rate:
    def __init__(self, format='value', diff = False):
        self.format = format
        self.diff = diff
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.diff == False:
                if self.format == 'value':
                    return response[currency]['Value']
            else:
                if self.format == "value":
                    return response[currency]["Value"]- response[currency]["Previous"]
            if self.format == "name":
                if currency == "EUR":
                    return "Euro"
                elif currency == "USD":
                    return "US Dollar"
        return 'Error'
    
    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

print(Rate('value', True).eur())



# Задание 5
# Напишите функцию, возвращающую сумму первых n чисел Фибоначчи

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# Задание 6
# Напишите функцию, преобразующую произвольный список вида 
# [‘2018-01-01’, ‘yandex’, ‘cpc’, 100] в словарь {‘2018-01-01’: {‘yandex’: {‘cpc’: 100}}}

list = ['2018-01-01', 'yandex', 'cpc', 100]

lenOfList = len(list)

def fn(list):
    global lenOfList
    if not list:
        return
    lenOfList = lenOfList - 1
    if lenOfList > 1:
        x = list[0]
        y = list[1:]
        return {x:fn(y)}
    else:
        print("check")
        x = list[0]
        y = list[1]
        return {x:y}


print(fn(list))

# В данном решении мне не понравилось что мне пришлось вынести переменную lenOfList
# из функции. Можно ли мне както было встроить ее в функцию?
