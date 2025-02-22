import datetime as dt
import numpy as np
import pandas as pd

# Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

def get_days_from_today(date = '2025-01-01'):
    try:
        in_date = dt.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:      # catch exception for wrong format value of date
        print('Wrong date format string, format YYYY-MM-DD needed!')
        return None
    now_date = dt.datetime.today()
    return (in_date - now_date).days

print(get_days_from_today("2021-10-09"))
print(type(get_days_from_today('0001-2-28'))) # type Integer


# Завдання 2
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
# яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. 

def get_numbers_ticket(min = 1, max = 36, quantity = 6):
    result = np.random.choice(range(max), quantity, replace=False)
    result.sort()
    result = result.tolist()    
    return result

print(get_numbers_ticket(1, 49, 6))
print(type(get_numbers_ticket())) # type List
    

# Завдання 3
# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку. 

def normalize_phone(phone_number):
    result = ''
    for c in phone_number: 
        if c in '0123456789': 
            result += c
    if result[0] == '0': 
        result = "+38" + result    
    elif result[0] == '3': 
        result = "+" + result
    else:
        result = f"Phone number {result} not from Ukrainian pool or wrong number!"

    return result

# check  
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", "48050 111 22 11   " # random number added with country code 480
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Завдання 4
# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
# Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. 
def next_birthday(birthday, date):
    if birthday.replace(year = date.year) >= date: 
        return birthday.replace(year = date.year)
    else:
        return birthday.replace(year = date.year + 1)

def get_upcoming_birthdays(users):
    result = []
    now_date = dt.datetime.now().date()
    users_df = pd.DataFrame(users)
    users_df['birthday'] =  users_df['birthday'].apply(lambda x: dt.datetime.strptime(x, '%Y.%m.%d').date())
    users_df['next_birthday'] = users_df['birthday'].apply(lambda x: next_birthday(x, now_date))
    users_df['delta'] = users_df['birthday'].apply(lambda x: (next_birthday(x, now_date) - now_date).days)
    for i, r in users_df.iterrows():
        if r['delta'] <= 7:
            congrats_date = r['next_birthday']
            if r['next_birthday'].weekday() in [5, 6]: 
                congrats_date = r['next_birthday'] + dt.timedelta(days=(7 - r['next_birthday'].weekday()))
            result.append({'name': f'{r['name']}', 'congratulation_date': f'{dt.datetime.strftime(congrats_date, '%Y-%m-%d')}'})

    return result

# check 
users = [
    {"name": "+John Doe", "birthday": "1985.02.23"},
    {"name": "+Jane Smith", "birthday": "1990.02.22"},
    {"name": "+Eva Smith", "birthday": "1985.02.24"},
    {"name": "-Mark Zukerberg", "birthday": "1990.01.27"}, 
    {"name": "+Bruce Willis", "birthday": "1985.03.01"},
    {"name": "+Jenifer Lopes", "birthday": "1990.02.28"},
    {"name": "-Michael Jackson", "birthday": "1985.02.20"},
    {"name": "-Ronald Reygan", "birthday": "1990.01.27"}
]    

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
print(dt.datetime.now().weekday())
    