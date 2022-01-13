from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class AttributeValueVarchar(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(255), nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.attribute_id'))
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.entity_type_id'))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
