from app import db
from app.models.Base import Base


class OrderSalesGroup(db.Model, Base):
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    group_entity_id = db.Column(db.Integer, db.ForeignKey('group_entity.group_entity_id'))
    order_sales_group = db.relationship('OrderSales', backref='order_sales_group', lazy="dynamic")
