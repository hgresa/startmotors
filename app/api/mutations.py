from datetime import datetime
from app.models.Salary import Salary
from app.models.Employees import Employees


def resolve_create_salary(obj, info, amount, pay_date, employee_id):
    try:
        pay_date = datetime.strptime(pay_date, '%d/%m/%Y').date()
        employee = Employees.query.get(employee_id)
        salary = Salary.create(amount=amount,
                               pay_date=pay_date,
                               employee_to_pay=employee)

        payload = {
            'success': True,
            'salary': salary.to_dict()
        }

    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload
