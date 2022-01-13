from app import db
from sqlalchemy import DateTime, func
from app.models.Base import Base


class Expense(db.Model, Base):
    expense_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paid_total = db.Column(db.Integer, nullable=False)
    pay_date = db.Column(DateTime(timezone=True), nullable=False)
    description = db.Column(db.String(10000))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_expense_id(self):
        return self.expense_id

    def get_paid_total(self):
        return self.paid_total

    def get_pay_date(self):
        return self.pay_date

    def get_description(self):
        return self.description

    def get_created_at(self):
        return self.create()

    def to_dict(self):
        return {
            'expense_id': self.get_expense_id(),
            'paid_total': self.get_paid_total(),
            'pay_date': self.get_pay_date(),
            'description': self.get_description(),
            'created_at': self.get_created_at()
        }
