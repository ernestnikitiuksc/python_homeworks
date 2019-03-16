# Задание 1
# Напишите функцию date_range, которая возвращает список дней между датами 
# start_date и end_date. Даты должны вводиться в формате YYYY-MM-DD.

from datetime import datetime
from datetime import timedelta

start_date = ""
end_date = ""
listOfDateRange = []

def date_range():
    print("input start date in format YYYY-MM-DD")
    start_date = input()
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        print("input end date in format YYYY-MM-DD")
        end_date = input()
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except:
            print("wrong input try again")
            date_range()
    except:
        print("wrong input try again")
        date_range()

    while start_date <= end_date:
        listOfDateRange.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
    print(listOfDateRange)


date_range()



# Задание 2
# Дополните функцию из первого задания проверкой на корректность дат. 
# В случае неверного формата или если start_date > end_date должен возвращаться пустой список.

from datetime import datetime
from datetime import timedelta

def date_range():
    start_date = ""
    end_date = ""
    listOfDateRange = []

    print("input start date in format YYYY-MM-DD")
    start_date = input()
    print("input end date in format YYYY-MM-DD")
    end_date = input()

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        while start_date <= end_date:
            listOfDateRange.append(start_date.strftime('%Y-%m-%d'))
            start_date += timedelta(days=1)
        print(listOfDateRange)
    except:
        print(listOfDateRange)


date_range()


# Задание 3
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой
# даты возвращает True (дата корректна) или False (некорректная дата).

from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']

def checkForCorrectDate(list):
    for i in list:
        try:
            datetime.strptime(i, '%Y-%m-%d')
            print(i, True)
        except:
            print(i, False)

checkForCorrectDate(stream)


# Задание 4
#
# Напишите функцию, которая возвращает список дат с 1 по вчерашний день текущего месяца.
# Если дан 1 день месяца, то возвращается список дней прошлого месяца.

from datetime import datetime
from datetime import timedelta

def my_function():
    correctionForNum1 = 0
    endDateAndTime = datetime.strftime(datetime.now(),"%Y-%m-%d")
    endDateAndTime = datetime.strptime(endDateAndTime, "%Y-%m-%d")
    startDate = endDateAndTime-timedelta(days=endDateAndTime.day -1 )
    if endDateAndTime.day == 1:
        endDateAndTime = endDateAndTime - timedelta(days=1)
        startDate = endDateAndTime-timedelta(days=endDateAndTime.day -1 )
        correctionForNum1 =1
    while startDate < endDateAndTime + timedelta(days = correctionForNum1):
        print (startDate.strftime("%Y-%m-%d"))
        startDate += timedelta(days=1)

my_function()


# Задание 5

# Напишите функцию, которая возвращает точную дату в формате YYYY-MM-DD по фразе:
# ‘today’ - сегодняшнюю дату
# ‘last monday’ - прошлый понедельник
# ‘last day’ - Последний день текущего месяца

from datetime import datetime
from datetime import timedelta


def date_returner():
    print("input: today / last monday / last day")
    command = input()
    cur_day = datetime.today()
    if command == "today":
        print( datetime.strftime(cur_day, "%Y-%m-%d") )
    elif command == "last monday":
        if cur_day.weekday() != 0:
            last_monday = cur_day - timedelta(cur_day.weekday())
        else:
            last_monday = cur_day - timedelta(cur_day.weekday()) - timedelta(days=7)
        print(datetime.strftime(last_monday, "%Y-%m-%d"))
    elif command == "last day":
        this_month = cur_day.month
        while cur_day.month == this_month:
            cur_day += timedelta(days=1)
        print(cur_day - timedelta(days=1))


date_returner()



