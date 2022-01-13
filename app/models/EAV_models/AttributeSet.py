from app import db
from app.models.Base import Base


class AttributeSet(db.Model, Base):
    attribute_set_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    attribute_set = db.relationship('Attribute', backref="attribute_set", lazy="dynamic")
    attribute_set_category = db.relationship('ProductCategories', backref='attribute_set_category', lazy='dynamic')

    def get_attribute_set_id(self):
        return self.attribute_set_id

    def get_label(self):
        return self.label

    def to_dict(self):
        return {
            'attribute_set_id': self.get_attribute_set_id(),
            'label': self.get_label()
        }
