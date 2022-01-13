from app import db
from sqlalchemy import DateTime, func
from app.models.Base import Base
from app.models.inventory_managemet_models.Product import Product
from app.models.inventory_managemet_models.ProductCategories import ProductCategories
from app.models.inventory_managemet_models.Stock import Stock
from app.models.inventory_managemet_models.Litres import Litres


class StockHistory(db.Model, Base):
    stock_history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Float)
    price_per_piece = db.Column(db.Float)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'))
    group_id = db.Column(db.Integer, db.ForeignKey('stock_history_group.group_id'))
    group_entity_id = db.Column(db.Integer, db.ForeignKey('group_entity.group_entity_id'))

    def get_fully_qualified_entries(self, product_category_name):
        SQL = self.query.with_entities(Product.product_name, ProductCategories.category_name, StockHistory.quantity,
                                       StockHistory.price_per_piece, StockHistory.total_price, StockHistory.created_at). \
            join(Stock, Stock.stock_id == StockHistory.stock_id). \
            join(Product, Stock.product_id == Product.product_id). \
            join(ProductCategories, ProductCategories.product_category_id == Product.product_category_id). \
            filter(ProductCategories.category_name == product_category_name). \
            order_by(StockHistory.created_at.desc()). \
            all()

        return SQL

    def get_litres_restock(self, product_category_name):
        SQL = self.query.with_entities(Product.product_name, ProductCategories.category_name, StockHistory.quantity,
                                       StockHistory.price_per_piece, StockHistory.total_price, StockHistory.created_at,
                                       Litres.quantity). \
            join(Litres, Litres.group_entity_id == StockHistory.group_entity_id). \
            join(Stock, Stock.stock_id == StockHistory.stock_id). \
            join(Product, Stock.product_id == Product.product_id). \
            join(ProductCategories, ProductCategories.product_category_id == Product.product_category_id). \
            filter(Litres.entity_id == StockHistory.stock_history_id,
                   ProductCategories.category_name == product_category_name). \
            order_by(StockHistory.created_at.desc()).all()

        return SQL
