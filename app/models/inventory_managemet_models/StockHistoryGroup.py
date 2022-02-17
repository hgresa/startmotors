from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class StockHistoryGroup(db.Model, Base):
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    group_entity_id = db.Column(db.Integer, db.ForeignKey('group_entity.group_entity_id'))
    history_group_stock = db.relationship('StockHistory', backref='history_group_stock', lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
