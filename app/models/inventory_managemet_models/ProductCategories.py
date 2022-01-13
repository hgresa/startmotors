from app import db
from app.models.Base import Base
from app.models.EAV_models.Attribute import Attribute


class ProductCategories(db.Model, Base):
    product_category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(255))
    product_category = db.relationship('Product', backref='product_category', lazy='dynamic')
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.entity_type_id'))
    attribute_set_id = db.Column(db.Integer, db.ForeignKey('attribute_set.attribute_set_id'))

    def get_attributes(self):
        return self.attribute_set_category.attribute_set.all()

    def get_product_categories(self):
        product_categories = self.query.all()

        return [i.category_name for i in product_categories]

    def get_attribute_set_id(self, to_filter, value):
        return self.query.filter(getattr(ProductCategories, to_filter) == value).first().attribute_set_id

    def is_litres_category(self):
        return True if self.attribute_set_category.attribute_set.filter(Attribute.label == "litres_quantity").first() \
            else False

    def get_category_name(self):
        return self.category_name

    def get_entity_type(self):
        return self.product_category_entity

    def get_attribute_set(self):
        return self.attribute_set_category

    # def get_data(self):
    #     self.data['product_category_id'] = self.product_category_id
    #     self.data['category_name'] = self.category_name
    #     self.data['entity_type_id'] = self.get_entity_type().entity_type_id
    #     self.data['entity_type_label'] = self.get_entity_type().label
    #     self.data['attribute_set_id'] = self.get_attribute_set().attribute_set_id
    #     self.data['attribute_set_label'] = self.get_attribute_set().label
    #
    #     return self.data
