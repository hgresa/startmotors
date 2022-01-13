from app import app
from flask import jsonify, request, render_template
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *


@app.route("/get_attributes", methods=["POST"])
def get_attributes():
    if request.method == "POST":
        category = ProductCategories.get(category_name=request.form["product_category"]).first()
        attribute_set_id = category.attribute_set_id
        entity_type_id = category.entity_type_id
        attribute_objects = Attribute.get(attribute_set_id=attribute_set_id,
                                          entity_type_id=entity_type_id).all()
        attribute_name_array = [i.label for i in attribute_objects]

        return jsonify(attribute_name_array)