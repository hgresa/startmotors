from app import db
from app.models.Base import Base


class MonthlyPaymentTypes(db.Model, Base):
    payment_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    payment_type = db.relationship("MonthlyPaymentValue", backref="payment_type", lazy='dynamic')
