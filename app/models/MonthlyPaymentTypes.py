from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class MonthlyPaymentTypes(db.Model, Base):
    payment_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    payment_type = db.relationship("MonthlyPaymentValue", backref="payment_type", lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_payment_type_id(self):
        return self.payment_type_id

    def get_label(self):
        return self.label

    def to_dict(self):
        return {
            'payment_type_id': self.get_payment_type_id(),
            'label': self.get()
        }
