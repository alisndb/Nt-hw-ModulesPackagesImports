from datetime import datetime

from application import salary
from application.db import people


def start():
    print(f'Accountant 0.1 successfully started!\nCurrent time: {datetime.now()}\n')
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    start()
