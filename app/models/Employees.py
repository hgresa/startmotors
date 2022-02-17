from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class Employees(db.Model, Base):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    full_name = db.ColumnProperty(name + " " + surname)
    employee_to_pay = db.relationship('Salary', backref='employee_to_pay', lazy='dynamic')
    employee_that_worked = db.relationship('CompletedWork', backref='employee_that_worked', lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_employees(self):
        return self.query.with_entities(Employees.employee_id,
                                        Employees.full_name).all()

    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.name

    def get_employee_surname(self):
        return self.surname

    def get_employee_fullname(self):
        return self.fullname

    def to_dict(self):
        return {
            'employee_id': self.get_employee_id(),
            'name': self.get_employee_name(),
            'surname': self.get_employee_surname(),
        }
