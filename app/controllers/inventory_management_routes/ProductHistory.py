from app import app
from flask import jsonify, request, render_template
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *


@app.route("/order_history", methods=["GET", "POST"])
def order_history():
    product_categories = [i.get_category_name() for i in ProductCategories.get()]
    if request.method == "POST":
        product_category = ProductCategories.get(category_name=request.form["product_category"]).first()

        if product_category.is_litres_category():
            order_sales = list(reversed(OrderSales.get_litres_orders(OrderSales(), product_category.category_name)))

            return render_template("order_sales.html", product_categories=product_categories,
                                   order_sales=order_sales,
                                   show_litres=True)
        else:
            order_sales = list(reversed(OrderSales.get_fully_qualified_entries(OrderSales(), product_category.category_name)))

            return render_template("order_sales.html", product_categories=product_categories, order_sales=order_sales)

    return render_template('order_sales.html', product_categories=product_categories)


@app.route("/restock_history", methods=["GET", "POST"])
def restock_history():
    product_categories = [i.get_category_name() for i in ProductCategories.get()]

    if request.method == "POST":
        product_category = ProductCategories.get(category_name=request.form["product_category"]).first()

        if product_category.is_litres_category():
            restock_history_list = StockHistory.get_litres_restock(StockHistory(), product_category.category_name)

            return render_template("restock_history.html",
                                   product_categories=product_categories,
                                   restock_history_list=restock_history_list,
                                   show_litres=True)
        else:
            restock_history_list = StockHistory.get_fully_qualified_entries(StockHistory(),
                                                                            product_category.category_name)

            return render_template("restock_history.html",
                                   product_categories=product_categories,
                                   restock_history_list=restock_history_list)

    return render_template('restock_history.html', product_categories=product_categories)
