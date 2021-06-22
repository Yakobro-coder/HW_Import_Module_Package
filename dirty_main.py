from application.salary import *
from application.db.people import *
from datetime import datetime

if __name__ == '__main__':
    date = datetime.now().strftime('%d-%m-%Y %H:%M')
    print(f'\nСегодня {date}')
    print()
    calculate_salary()
    get_employees()
