from datetime import datetime

from application.salary import *
from application.db.people import *


def start():
    print(f'Accountant 0.1 successfully started!\nCurrent time: {datetime.now()}\n')
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    start()
