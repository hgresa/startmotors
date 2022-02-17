from app import db
from app.models.Base import Base
from sqlalchemy import DateTime, func


class Stock(db.Model, Base):
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price_per_piece = db.Column(db.Float)
    stock_qty = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    stock_entry = db.relationship('StockHistory', backref='stock_entry', lazy='dynamic')
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())

    def get_current_id(self):
        return self.stock_id

    def get_price_per_piece(self, product_id):
        return self.query.filter_by(product_id=product_id).first().price_per_piece
