from app import db
from app.models.Base import Base


class DataTypes(db.Model, Base):
    data_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)
    data_type = db.relationship('Attribute', backref='data_type', lazy='dynamic')

    def get_data_type_id(self):
        return self.data_type_id

    def get_label(self):
        return self.label

    def to_dict(self):
        return {
            'data_type_id': self.get_data_type_id(),
            'label': self.get_label()
        }
