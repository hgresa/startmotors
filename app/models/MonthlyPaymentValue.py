from app import db
from sqlalchemy import func
from app.models.MonthlyPaymentTypes import MonthlyPaymentTypes
from app.models.Base import Base


class MonthlyPaymentValue(db.Model, Base):
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, nullable=False)
    pay_date = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    type_id = db.Column(db.Integer, db.ForeignKey('monthly_payment_types.payment_type_id'))

    def get_fully_qualified_values(self):
        return self.query.with_entities(MonthlyPaymentTypes.label,
                                        MonthlyPaymentValue.value,
                                        MonthlyPaymentValue.pay_date,
                                        MonthlyPaymentValue.created_at). \
            join(MonthlyPaymentTypes, MonthlyPaymentTypes.payment_type_id == MonthlyPaymentValue.type_id).all()

    def get_payment_id(self):
        return self.payment_id

    def get_value(self):
        return self.value

    def get_pay_date(self):
        return self.pay_date

    def get_created_at(self):
        return self.created_at

    def get_payment_type(self):
        return self.payment_type

    def to_dict(self):
        return {
            'payment_id': self.get_payment_id(),
            'value': self.get_value(),
            'pay_date': self.get_pay_date(),
            'created_at': self.get_created_at(),
            'type': self.get_payment_type()
        }
