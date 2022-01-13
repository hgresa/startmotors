from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func
from app.models.inventory_managemet_models.Product import Product


class AttributeValueInteger(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Integer, nullable=False)
    entity_id = db.Column(db.Integer, nullable=False)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.attribute_id'))
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.entity_type_id'))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value

    def get_attribute(self):
        return self.attribute_int

    def get_entity_id(self):
        return self.entity_id

    def get_entity_type_id(self):
        return self.entity_type_id

    def get_entity_type(self):
        return self.attr_value_integer_entity_type

    def get_created_at(self):
        return self.created_at
