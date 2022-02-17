from app import db
from sqlalchemy import DateTime, func, between
from app.models.Employees import Employees
from app.models.Base import Base


class Salary(db.Model, Base):
    salary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    pay_date = db.Column(DateTime(timezone=True), nullable=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))

    def get_fully_qualified_salaries(self):
        query = self.query.with_entities(Employees.name,
                                         Employees.surname,
                                         Salary.amount,
                                         Salary.pay_date,
                                         Salary.created_at). \
            join(Employees, Employees.employee_id == Salary.employee_id).all()

        return query

    def get_salary_sum(self, from_date, to_date):
        return self.query.with_entities(func.sum(Salary.amount)).filter(Salary.pay_date.between(from_date, to_date))

    def get_salary_id(self):
        return self.salary_id

    def get_amount(self):
        return self.amount

    def get_pay_date(self):
        return self.pay_date

    def get_created_at(self):
        return self.created_at

    def get_employee(self):
        return self.employee_to_pay

    def to_dict(self):
        return {
            'salary_id': self.get_salary_id(),
            'amount': self.get_amount(),
            'pay_date': self.get_pay_date(),
            'created_at': self.get_created_at(),
            'employee': self.get_employee()
        }
