from app import app
from flask import jsonify, request, render_template, make_response
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *
import json


def insert_product(litres, quantity, price_per_piece, purchase_price, total_price,
                   product_name, product_category, product_entity, attributes, form):
    product = Product.create(product_name=product_name,
                             product_category=product_category,
                             product_entity=product_entity)
    product_entity_type = EntityType.get(label='product').first()

    for item in attributes:
        attribute_label = item.label
        value = form[attribute_label]

        if item.get_data_type_label() == 'integer':
            if attribute_label == "car_model_id":
                for i in value:
                    value = CarModels.get(car_model_name=i).first().car_model_id
                    AttributeValueInteger.create(value=value,
                                                 entity_id=product.product_id,
                                                 attr_value_integer_entity_type=product_entity_type,
                                                 attribute_int=item)
            else:
                AttributeValueInteger.create(value=value,
                                             entity_id=product.product_id,
                                             attr_value_integer_entity_type=product_entity_type,
                                             attribute_int=item)

        elif item.get_data_type_label() == 'varchar':
            AttributeValueVarchar.create(value=value,
                                         entity_id=product.product_id,
                                         attr_value_varchar_entity_type=product_entity_type,
                                         attribute_var=item)

    stock = Stock.create(price_per_piece=price_per_piece,
                         stock_qty=quantity,
                         product_stock=product)

    stock_history_group_entity = GroupEntity.get(label='stock_history_group').first()
    history_group = StockHistoryGroup.get(label='default' if not litres else 'litres').first()

    stock_history = StockHistory.create(quantity=quantity,
                                        total_price=total_price,
                                        price_per_piece=purchase_price,
                                        stock_entry=stock,
                                        history_group_stock=history_group,
                                        history_group=stock_history_group_entity)

    if product.is_litres_product():
        Litres.create(quantity=litres,
                      entity_id=stock_history.stock_history_id,
                      group_entity_litres=stock_history_group_entity)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    success = False

    if request.args.get('success') == "1":
        success = True

    if request.method == "POST":
        form = {}

        for value in json.loads(request.form['form']):
            form[value['name']] = value['value']

        if request.form['car_model_id']:
            form['car_model_id'] = list(set(json.loads(request.form['car_model_id'])))

        success = True
        litres = form.get('litres_quantity', None)
        quantity = form['quantity']
        price_per_piece = float(form['price_per_piece'])
        purchase_price = float(form['purchase_price_per_piece'])
        total_price = float(quantity) * float(purchase_price)
        product_name = form["product_name"]
        product_category_name = form['product_category']
        product_category = ProductCategories.get(category_name=product_category_name).first()
        product_entity = EntityType.get(label='product').first()
        attributes = product_category.get_attributes()

        if litres:
            total_price = purchase_price
            for i in range(0, int(quantity), 1):
                insert_product(litres, 0, price_per_piece, purchase_price, total_price,
                               product_name, product_category, product_entity, attributes, form)
        else:
            insert_product(litres, quantity, price_per_piece, purchase_price, total_price,
                           product_name, product_category, product_entity, attributes, form)

    product_categories = [i.get_category_name() for i in ProductCategories.get().all()]

    return render_template('add_product.html', product_categories=product_categories, success=success)


@app.route("/sell_product", methods=["POST"])
def sell_product():
    if request.method == "POST":
        litres = request.form.get('litres', None)
        quantity = int(request.form["quantity"])
        price_per_piece = float(request.form['price_per_piece'])
        total_price = quantity * price_per_piece

        product = Product.get(product_id=request.form['product_id']).first()
        group_entity = GroupEntity.get(label='order_sales_group').first()
        order_sales_group = OrderSalesGroup.get(label='litres' if litres else 'default').first()

        order_sale = OrderSales.create(quantity=quantity,
                                       price_per_piece=price_per_piece,
                                       sold_for_total=total_price,
                                       product_on_order=product,
                                       order_sales_group=order_sales_group,
                                       order_sales_group_entity=group_entity)

        if product.is_litres_product():
            Litres.create(quantity=litres,
                          entity_id=order_sale.order_sale_id,
                          group_entity_litres=group_entity)

            litres_attribute = product.get_litres_attribute()
            new_litres_value = litres_attribute.value - int(litres)
            litres_attribute.update(value=new_litres_value)
            quantity = 0

        stock = product.product_stock.first()
        stock.update(stock_qty=stock.stock_qty - quantity)

        return make_response(jsonify({'message': 'Done', 'code': 'SUCCESS'}))


@app.route("/buy_product", methods=["POST"])
def buy_product():
    if request.method == "POST":
        product_id = request.form['product_id']
        litres = request.form.get('litres', None)
        quantity = int(request.form["quantity"]) if not litres else 0
        price_per_piece = float(request.form['price_per_piece'])
        total_price = int(request.form["quantity"]) * price_per_piece

        product = Product.get(product_id=product_id).first()
        stock = product.product_stock.first()
        stock_history_group_entity = GroupEntity.get(label='stock_history_group').first()
        history_group = StockHistoryGroup.get(label='default' if not litres else 'litres').first()

        stock.update(stock_qty=stock.stock_qty + quantity)
        stock_history = StockHistory.create(quantity=quantity,
                                            total_price=total_price,
                                            price_per_piece=price_per_piece,
                                            stock_entry=stock,
                                            history_group_stock=history_group,
                                            history_group=stock_history_group_entity)

        if product.is_litres_product():
            Litres.create(quantity=litres,
                          entity_id=stock_history.stock_history_id,
                          group_entity_litres=stock_history_group_entity)

            litres_attribute = product.get_litres_attribute()
            new_litres_value = litres_attribute.value + int(litres)
            litres_attribute.update(value=new_litres_value)

        return make_response(jsonify({"code": 200}))


@app.route("/list_product", methods=["GET", "POST"])
def list_product():
    product_categories = [i.get_category_name() for i in ProductCategories.get().all()]

    if request.method == "POST":
        products = get_fully_qualified_products()

        product_category = request.form["product_category"]

        return render_template('products.html', products=products,
                               product_categories=product_categories,
                               product_category=product_category)

    return render_template('products.html', product_categories=product_categories)


@app.route("/get_products", methods=["POST"])
def get_fully_qualified_products():
    if request.method == "POST":
        product_category = ProductCategories.get(category_name=request.form["product_category"]).first()
        attributes = product_category.get_attributes()
        attribute_labels = sorted([i.label for i in attributes])
        unified_products = Product.get_fully_qualified_products(Product(), request.form["product_category"])

        for key, value in unified_products.items():
            if 'car_model_id' in value:
                car_model_ids = value['car_model_id'].split(',')
                car_model_names = ""
                for _id in car_model_ids:
                    car_model_name = CarModels.get(car_model_id=_id).first().get_car_model_name()
                    car_model_names += ', ' + car_model_name

                unified_products[key]['car_model_id'] = car_model_names[1:]

        return {"titles": attribute_labels, "attribute_entities": list(unified_products.values())}
