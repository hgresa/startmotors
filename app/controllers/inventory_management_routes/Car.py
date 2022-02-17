from app import app
from app import db
from flask import jsonify, request, render_template
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *


@app.route("/get_car_categories", methods=["GET", "POST"])
def get_car_categories():
    car_categories = [i.get_car_category_name() for i in CarCategories.get()]

    return jsonify(car_categories)


@app.route("/add_cars", methods=["GET"])
def add_cars():
    car_categories = [car_category.to_dict() for car_category in CarCategories.query.all()]
    return render_template("add_car.html", car_categories=car_categories)
