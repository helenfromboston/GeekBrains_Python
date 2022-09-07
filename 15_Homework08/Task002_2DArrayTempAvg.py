# Задача 3. В двумерном массиве хранятся средние дневные температуры
# с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

import calendar
import random
from statistics import mean

def fill_months(year, first_month, last_month):
    cal = calendar.Calendar(firstweekday=0)
    res = []
    res_new = []
    for month in range(first_month, last_month):
        res = list(calendar.Calendar.itermonthdays4(cal, year, month))
        for day in range(calendar.month(year, month).count('\n') - 2):
            if res[(7*day):(7*day+7)] not in res_new:
                res_new.append(res[(7*day):(7*day+7)])
    return res_new

def weeks_avg_temp(weeks_list):
    temp = [0]*len(weeks_list)
    temp_avg_list = []
    for i in range(len(temp)):
        temp[i] = list(random.randint(15, 30) for j in range(7))
        temp_avg_list.append(round(mean(temp[i]), 1))
    return temp_avg_list

def find_hold_cold(temp_avg_list):
    hot_week = max(temp_avg_list)
    hot_week_index = temp_avg_list.index(hot_week)
    cold_week = min(temp_avg_list)
    cold_week_index = temp_avg_list.index(cold_week)
    return hot_week, hot_week_index, cold_week, cold_week_index

user_months = fill_months(2021, 5, 10)
for i in user_months:
    print(i)
print()

temp_avg_list = weeks_avg_temp(user_months)
print(temp_avg_list)
print()

indices = list(find_hold_cold(temp_avg_list))
print(indices)
print()

print(f"Самая жаркая неделя: {user_months[indices[1]][0][2]}.{user_months[indices[1]][0][1]}.\
{user_months[indices[1]][0][0]} - {user_months[indices[1]][6][2]}.{user_months[indices[1]][6][1]}.\
{user_months[indices[1]][6][0]} (средняя температура {indices[0]}°C)")

print(f"Самая холодная неделя: {user_months[indices[3]][0][2]}.{user_months[indices[3]][0][1]}.\
{user_months[indices[3]][0][0]} - {user_months[indices[3]][6][2]}.{user_months[indices[3]][6][1]}.\
{user_months[indices[3]][6][0]} (средняя температура {indices[2]}°C)")