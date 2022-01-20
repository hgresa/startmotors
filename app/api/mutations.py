from datetime import datetime
from app.models.Salary import Salary
from app.models.Employees import Employees
from app.models.inventory_managemet_models.Product import Product
from app.models.inventory_managemet_models.ProductCategories import ProductCategories
from app.models.EAV_models.EntityType import EntityType
from app.models.EAV_models.AttributeValueVarchar import AttributeValueVarchar
from app.models.EAV_models.AttributeValueInteger import AttributeValueInteger


def resolve_create_salary(obj, info, amount, pay_date, employee_id):
    try:
        pay_date = datetime.strptime(pay_date, '%d/%m/%Y').date()
        employee = Employees.query.get(employee_id)
        salary = Salary.create(amount=amount,
                               pay_date=pay_date,
                               employee_to_pay=employee)

        payload = {
            'success': True,
            'salary': salary.to_dict()
        }

    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_create_product(obj, info, product_name, product_category_name):
    try:
        product_category = ProductCategories.get(category_name=product_category_name).first()
        product_entity_type = EntityType.get(label='product').first()
        product = Product.create(product_name=product_name,
                                 product_category=product_category,
                                 product_entity=product_entity_type)

        payload = {
            'success': True,
            'product': product.to_dict()
        }

    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_create_attribute_value(obj, info, attribute_label, attribute_value, product_id):
    product = Product.query.get(product_id)
    attributes = product.get_product_category().get_attributes()

    for attribute in attributes:
        if attribute.get_label() == attribute_label:
            data_type = attribute.get_data_type_label()

            if data_type == 'varchar':
                AttributeValueVarchar.create(value=attribute_value,
                                             entity_id=product.get_product_id(),
                                             attr_value_integer_entity_type=product.get_entity_type(),
                                             attribute_var=attribute)

            elif data_type == 'integer':
                if attribute_label == "car_model_id":
                    pass

                AttributeValueInteger.create(value=attribute_value,
                                             entity_id=product.get_product_id(),
                                             attr_value_integer_entity_type=product.get_entity_type(),
                                             attribute_var=attribute)
