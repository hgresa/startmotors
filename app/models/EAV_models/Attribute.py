from app import db
from app.models.Base import Base


class Attribute(db.Model, Base):
    attribute_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    data_type_id = db.Column(db.Integer, db.ForeignKey('data_types.data_type_id'))
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.entity_type_id'))
    attribute_set_id = db.Column(db.Integer, db.ForeignKey('attribute_set.attribute_set_id'))
    attribute_var = db.relationship('AttributeValueVarchar', backref="attribute_var", lazy="dynamic")
    attribute_int = db.relationship('AttributeValueInteger', backref="attribute_int", lazy="dynamic")

    def get_data_type_label(self):
        return self.data_type.label

    def get_attribute_id(self):
        return self.attribute_id

    def get_label(self):
        return self.label

    def get_data_type(self):
        return self.data_type

    def get_entity_type(self):
        return self.entity_type

    def get_attribute_set(self):
        return self.attribute_set

    def to_dict(self):
        return {
            'attribute_id': self.get_attribute_id(),
            'label': self.get_label(),
            'data_type': self.get_data_type(),
            'entity_type': self.get_entity_type(),
            'attribute_set': self.get_attribute_set()
        }
