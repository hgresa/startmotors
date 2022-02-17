from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class GroupEntity(db.Model, Base):
    group_entity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    group_entity_history = db.relationship('StockHistoryGroup', backref='group_entity_history', lazy='dynamic')
    group_entity_order = db.relationship('OrderSalesGroup', backref='group_entity_order', lazy='dynamic')
    history_group = db.relationship('StockHistory', backref='history_group')
    order_sales_group_entity = db.relationship('OrderSales', backref='order_sales_group_entity', lazy='dynamic')
    group_entity_litres = db.relationship('Litres', backref='group_entity_litres', lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_group_entity_id(self):
        return self.group_entity_id
