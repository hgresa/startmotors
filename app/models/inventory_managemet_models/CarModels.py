from app import db
from app.models.Base import Base


class CarModels(db.Model, Base):
    car_model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_model_name = db.Column(db.String(255))
    car_category_id = db.Column(db.Integer, db.ForeignKey('car_categories.car_category_id'))
    car_model = db.relationship('CompletedWork', backref='car_model', lazy='dynamic')

    def get_car_model_id(self):
        return self.car_model_id

    def get_car_model_name(self):
        return self.car_model_name

    def get_car_category(self):
        return self.model

    def to_dict(self):
        return {
            'car_model_id': self.get_car_model_id(),
            'car_model_name': self.get_car_model_name(),
            'car_category': self.get_car_category()
        }
