from app.models.Expense import Expense
from app.models.Salary import Salary
from app.models.Employees import Employees
from app.models.MonthlyPaymentValue import MonthlyPaymentValue
from app.models.MonthlyPaymentTypes import MonthlyPaymentTypes
from app.models.inventory_managemet_models.CarModels import CarModels
from app.models.inventory_managemet_models.CarCategories import CarCategories
from sqlalchemy import desc, asc
import sys


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def build_query(filters, class_name):
    order_by = filters.get('order_by', {'sort_by': 'created_at', 'sort_type': 'desc'})
    sort_by = order_by.get('sort_by', 'created_at')
    sort_type = order_by.get('sort_type', 'desc').lower()

    _class = str_to_class(class_name)
    query = _class.query

    if sort_type == 'desc':
        query = _class.query.order_by(desc(f'{sort_by}'))
    elif sort_type == 'asc':
        query = _class.query.order_by(asc(f'{sort_by}'))

    return query.all()


def resolve_salaries(obj, info, **filters):
    try:
        query = build_query(filters, Salary.__name__)
        salaries = [salary.to_dict() for salary in query]
        payload = {
            'success': True,
            'salaries': salaries
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_salary(obj, info, salary_id):
    try:
        salary = Salary.query.get(salary_id).to_dict()
        payload = {
            'success': True,
            'salary': salary
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'employee matching id {salary_id} not found']
        }

    return payload


def resolve_employees(obj, info):
    try:
        employees = [employee.to_dict() for employee in Employees.query.all()]
        payload = {
            'success': True,
            'employees': employees
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_employee(obj, info, employee_id):
    try:
        employee = Employees.query.get(employee_id)
        payload = {
            'success': True,
            'employee': employee
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'employee matching id {employee_id} not found']
        }

    return payload


def resolve_expenses(obj, info):
    try:
        expenses = [expense.to_dict() for expense in Expense.query.all()]
        payload = {
            'success': True,
            'expenses': expenses
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_expense(obj, info, expense_id):
    try:
        expense = Expense.query.get(expense_id)
        payload = {
            'success': True,
            'expense': expense
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'employee matching id {expense_id} not found']
        }

    return payload


def resolve_monthly_payment_value(obj, info, payment_id):
    try:
        monthly_payment_value = MonthlyPaymentValue.query.get(payment_id).to_dict()
        payload = {
            'success': True,
            'monthly_payment_value': monthly_payment_value
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'monthly payment value matching id {payment_id} not found']
        }

    return payload


def resolve_monthly_payment_values(obj, info, **filters):
    try:
        query = build_query(filters, MonthlyPaymentValue.__name__)
        monthly_payment_values = [mpv.to_dict() for mpv in query]
        payload = {
            'success': True,
            'monthly_payment_values': monthly_payment_values
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_monthly_payment_type(obj, info):
    pass


def resolve_monthly_payment_types(obj, info, **filters):
    try:
        query = build_query(filters, MonthlyPaymentTypes.__name__)
        monthly_payment_types = [mpt.to_dict() for mpt in query]

        payload = {
            'success': True,
            'monthly_payment_types': monthly_payment_types
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_car_category(obj, info, car_category_id):
    try:
        car_category = CarCategories.query.get(car_category_id).to_dict()
        payload = {
            'success': True,
            'car_category': car_category
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'car category matching id {car_category_id} not found']
        }

    return payload


def resolve_car_categories(obj, info):
    try:
        car_categories = [car_category.to_dict() for car_category in CarCategories.query.all()]
        payload = {
            'success': True,
            'car_categories': car_categories
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_car_model(obj, info, car_model_id):
    try:
        car_model = CarModels.query.get(car_model_id).to_dict()
        payload = {
            'success': True,
            'car_model': car_model
        }
    except AttributeError:
        payload = {
            'success': False,
            'errors': [f'car model matching id {car_model_id} not found']
        }

    return payload
