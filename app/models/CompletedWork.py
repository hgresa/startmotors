from app import db
from sqlalchemy import DateTime
from sqlalchemy import func
from app.models.Base import Base


class CompletedWork(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paid_total = db.Column(db.Integer, nullable=False)
    pay_date = db.Column(DateTime(timezone=True), nullable=False)
    description = db.Column(db.String(10000))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))
    car_model_id = db.Column(db.Integer, db.ForeignKey('car_models.car_model_id'))

    def get_paid_total(self):
        return self.paid_total

    def get_pay_date(self):
        return self.pay_date

    def get_description(self):
        return self.description

    def get_employee_name(self):
        return self.employee_that_worked.name

    def get_employee_surname(self):
        return self.employee_that_worked.surname

    def get_employee_fullname(self):
        return self.employee_that_worked.full_name

    def get_car_model(self):
        return self.car_model.car_model_name

    def get_created_at(self):
        return self.created_at
