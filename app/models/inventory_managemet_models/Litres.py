from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class Litres(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer, nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    group_entity_id = db.Column(db.Integer, db.ForeignKey('group_entity.group_entity_id'))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_quantity(self):
        return self.quantity
