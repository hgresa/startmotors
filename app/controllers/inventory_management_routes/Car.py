from app import app
from app import db
from flask import jsonify, request, render_template
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *


@app.route("/get_car_models", methods=["GET", "POST"])
def get_car_models():
    car_category_name = request.form["car_category_name"]
    # car_category_name = request.args.get('car_category_name')
    car_category = CarCategories.get(car_category_name=car_category_name).first()
    car_models = car_category.get_car_models()
    names = [i.get_car_model_name() for i in car_models]

    return jsonify(names)


@app.route("/get_car_categories", methods=["GET", "POST"])
def get_car_categories():
    car_categories = [i.get_car_category_name() for i in CarCategories.get()]

    return jsonify(car_categories)


@app.route("/add_cars", methods=["POST", "GET"])
def add_cars():
    if request.method == "POST":
        car_brand = request.form.get('car_brand').lower()
        new_car_models = request.form.get("new_car_models").split(",")

        if car_brand.isdigit():
            car_category = CarCategories.query.get(car_brand)
        else:
            car_category = CarCategories.create(car_category_name=car_brand)

        for car_model_name in new_car_models:
            CarModels.create(car_model_name=car_model_name.lower(), model=car_category)

    car_categories = [car_category.to_dict() for car_category in CarCategories.query.all()]
    return render_template("add_car.html", car_categories=car_categories)
