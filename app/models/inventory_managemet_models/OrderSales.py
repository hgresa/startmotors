from sqlalchemy import DateTime, func
from app import db
from app.models.Base import Base
from app.models.inventory_managemet_models.Litres import Litres
from app.models.inventory_managemet_models.Product import Product
from app.models.inventory_managemet_models.ProductCategories import ProductCategories


class OrderSales(db.Model, Base):
    order_sale_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    price_per_piece = db.Column(db.Float)
    sold_for_total = db.Column(db.Float)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    group_id = db.Column(db.Integer, db.ForeignKey('order_sales_group.group_id'))
    group_entity_id = db.Column(db.Integer, db.ForeignKey('group_entity.group_entity_id'))

    def get_quantity(self):
        return self.quantity

    def get_price_per_piece(self):
        return self.price_per_piece

    def get_sold_for_total(self):
        return self.sold_for_total

    def get_created_at(self):
        return self.created_at

    def get_product_name(self):
        return self.get_product().get_product_name()

    def get_product_category_name(self):
        return self.get_product().get_category().get_category_name()

    def get_litres_quantity(self):
        return self.get_litres().get_quantity()

    def get_product(self):
        return self.product_on_order

    def get_sales_group(self):
        return self.order_sales_group

    def get_group_entity(self):
        return self.order_sales_group_entity

    def get_litres(self):
        return Litres.get(group_entity_id=self.get_group_entity().get_group_entity_id(),
                          entity_id=self.order_sale_id).first()

    def get_fully_qualified_entries(self, product_category_name):
        query = self.query. \
            join(Product, OrderSales.product_id == Product.product_id). \
            join(ProductCategories, Product.product_category_id == ProductCategories.product_category_id). \
            filter(ProductCategories.category_name == product_category_name). \
            all()

        return query

    def get_litres_orders(self, product_category_name):
        query = self.query. \
            join(Litres, Litres.group_entity_id == OrderSales.group_entity_id). \
            join(Product, OrderSales.product_id == Product.product_id). \
            join(ProductCategories, Product.product_category_id == ProductCategories.product_category_id). \
            filter(ProductCategories.category_name == product_category_name,
                   Litres.entity_id == OrderSales.order_sale_id). \
            all()

        return query
