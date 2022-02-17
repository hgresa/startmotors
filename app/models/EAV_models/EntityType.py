from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class EntityType(db.Model, Base):
    entity_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    entity_type = db.relationship('Attribute', backref="entity_type", lazy="dynamic")
    product_category_entity = db.relationship('ProductCategories', backref="product_category_entity", lazy="dynamic")
    product_entity = db.relationship('Product', backref='product_entity', lazy="dynamic")
    attr_value_varchar_entity_type = db.relationship('AttributeValueVarchar', backref='attr_value_varchar_entity_type',
                                                     lazy='dynamic')
    attr_value_integer_entity_type = db.relationship('AttributeValueInteger', backref='attr_value_integer_entity_type',
                                                     lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_entity_type_id(self):
        return self.get_entity_type_id

    def get_label(self):
        return self.label

    def to_dict(self):
        return {
            'entity_type_id': self.get_entity_type_id(),
            'label': self.get_label()
        }
