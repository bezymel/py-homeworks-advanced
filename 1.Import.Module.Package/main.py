import application.salary as salary
import application.db.people as people
import datetime

if __name__ == '__main__':
    print("Текущая дата:", datetime.datetime.now())
    print("Расчет зарплаты:", salary.calculate_salary())
    print("Список сотрудников:", people.get_employees())
