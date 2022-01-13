from app import db
from app.models.Base import Base


class CarCategories(db.Model, Base):
    car_category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_category_name = db.Column(db.String(255))
    car_models = db.relationship('CarModels', backref='model', lazy='dynamic')

    def get_car_category_id(self):
        return self.car_category_id

    def get_car_category_name(self):
        return self.car_category_name

    def get_car_models(self):
        return self.car_models.all()

    def to_dict(self):
        return {
            'car_category_id': self.get_car_category_id(),
            'car_category_name': self.get_car_category_name(),
            'car_models': self.get_car_models()
        }
