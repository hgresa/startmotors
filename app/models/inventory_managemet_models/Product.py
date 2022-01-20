from app import db
from sqlalchemy import union_all
from app.models.Base import Base
# from app.models.EAV_models.AttributeValueVarchar import AttributeValueVarchar
# from app.models.EAV_models.AttributeValueInteger import AttributeValueInteger
from app.models.inventory_managemet_models import ProductCategories
# from app.models.EAV_models.Attribute import Attribute
from app.models.inventory_managemet_models import Stock
from sqlalchemy import DateTime, func
from app.models.EAV_models import AttributeValueVarchar
from app.models.EAV_models import AttributeValueInteger
from app.models.EAV_models import Attribute


class Product(db.Model, Base):
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255))
    product_stock = db.relationship('Stock', backref='product_stock', lazy='dynamic')
    product_on_order = db.relationship('OrderSales', backref='product_on_order', lazy='dynamic')
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.entity_type_id'))
    product_category_id = db.Column(db.Integer, db.ForeignKey('product_categories.product_category_id'))
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_fully_qualified_products(self, product_category_name):
        varchar_values = AttributeValueVarchar.AttributeValueVarchar.query
        integer_values = AttributeValueInteger.AttributeValueInteger.query
        unified_values = union_all(varchar_values, integer_values)
        subquery = unified_values.subquery()

        unified_attributes = self.query.with_entities(Product.product_id,
                                                      Product.product_name,
                                                      Attribute.label,
                                                      subquery.c.attribute_value_varchar_value). \
            join(ProductCategories.ProductCategories, ProductCategories.ProductCategories.product_category_id == Product.product_category_id). \
            join(Attribute, Attribute.attribute_set_id == ProductCategories.ProductCategories.attribute_set_id). \
            join(subquery, subquery.c.attribute_value_varchar_attribute_id == Attribute.attribute_id). \
            filter(ProductCategories.ProductCategories.category_name == product_category_name,
                   subquery.c.attribute_value_varchar_entity_id == Product.product_id). \
            order_by(Attribute.label). \
            all()

        product_dict = {}

        for i in unified_attributes:
            product_id = i[0]
            product_name = i[1]
            attribute_label = i[2]
            attribute_value = i[3]

            if product_dict.get(product_id):
                if attribute_label in product_dict[product_id]:
                    product_dict[product_id][attribute_label] += ',' + attribute_value
                else:
                    product_dict[product_id][attribute_label] = attribute_value
            else:
                product_dict[product_id] = {"product_id": product_id,
                                            "product_name": product_name,
                                            attribute_label: attribute_value}

        for key, value in product_dict.items():
            stock = Stock.Stock.get(product_id=key).first()
            stock_qty = stock.stock_qty
            price_per_piece = stock.price_per_piece
            value["stock"] = stock_qty
            value["price_per_piece"] = price_per_piece

        return product_dict

    def get_attribute_set(self):
        return self.product_category.attribute_set_category

    def get_attributes(self):
        return self.get_attribute_set().attribute_set.all()

    def get_litres_attribute(self):
        litres_attribute = self.product_category. \
            attribute_set_category. \
            attribute_set.filter(Attribute.label == "litres_quantity").first()

        if litres_attribute:
            return litres_attribute. \
                attribute_int. \
                filter(AttributeValueInteger.AttributeValueInteger.entity_id == self.product_id).first()

        return None

    def is_litres_product(self):
        if self.get_litres_attribute():
            return True

        return False

    def get_category(self):
        return self.product_category

    def get_category_name(self):
        return self.get_category().get_category_name()

    def get_product_name(self):
        return self.product_name

    def get_product_id(self):
        return self.product_id

    def get_entity_type(self):
        return self.product_entity

    def get_product_category(self):
        return self.product_category

    def to_dict(self):
        return {
            'product_id': self.get_product_id(),
            'product_name': self.get_product_name(),
            'entity_type': self.get_entity_type(),
            'product_category': self.get_product_category()
        }
