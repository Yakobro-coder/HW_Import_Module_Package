from application import salary
from application.db import people
from datetime import datetime

if __name__ == '__main__':
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    print(f'\nСегодня {date}')
    print()
    salary.calculate_salary()
    people.get_employees()

