from datetime import datetime
from app.models.Salary import Salary
from app.models.Employees import Employees
from app.models.MonthlyPaymentValue import MonthlyPaymentValue
from app.models.MonthlyPaymentTypes import MonthlyPaymentTypes
from app.models.inventory_managemet_models.Product import Product
from app.models.inventory_managemet_models.ProductCategories import ProductCategories
from app.models.inventory_managemet_models.CarCategories import CarCategories
from app.models.inventory_managemet_models.CarModels import CarModels
from app.models.EAV_models.EntityType import EntityType
from app.models.EAV_models.AttributeValueVarchar import AttributeValueVarchar
from app.models.EAV_models.AttributeValueInteger import AttributeValueInteger


def resolve_create_cars(obj, info, car_brand: str, new_car_models: str):
    try:
        car_brand = car_brand.lower()
        new_car_models = new_car_models.split(',')

        if car_brand.isdigit():
            car_category = CarCategories.query.get(car_brand)
        else:
            car_category = CarCategories.create(car_category_name=car_brand)

        for car_model_name in new_car_models:
            CarModels.create(car_model_name=car_model_name.lower(),
                             model=car_category)

        payload = {
            'success': True
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


def resolve_create_salary(obj, info, amount: float, pay_date: str, employee_id: int):
    try:
        pay_date = datetime.strptime(pay_date, '%Y-%m-%d').date()
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


def resolve_create_product(obj, info, product_name: str, product_category_name: str):
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


def resolve_create_monthly_payment_value(obj, info, amount: float, pay_date: str, payment_type: str):
    try:
        pay_date = datetime.strptime(pay_date, '%Y-%m-%d').date()
        payment_type = MonthlyPaymentTypes.get(label=payment_type).first()
        payment = MonthlyPaymentValue.create(
            value=amount,
            pay_date=pay_date,
            payment_type=payment_type
        )

        payload = {
            'success': True,
            'monthly_payment_value': payment.to_dict()
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [error]
        }

    return payload


def resolve_create_attribute_value(obj, info, attribute_label: str, attribute_value: str, product_id: int):
    try:
        product = Product.query.get(product_id)
        attributes = product.get_product_category().get_attributes()

        payload = {}

        for attribute in attributes:
            if attribute.get_label() == attribute_label:
                data_type = attribute.get_data_type_label()

                if data_type == 'varchar':
                    AttributeValueVarchar.create(value=attribute_value,
                                                 entity_id=product.get_product_id(),
                                                 attr_value_integer_entity_type=product.get_entity_type(),
                                                 attribute_var=attribute)
                    payload = {
                        'success': True,
                    }

                    break
                elif data_type == 'integer':
                    if attribute_label == "car_model_id":
                        pass

                    AttributeValueInteger.create(value=int(attribute_value),
                                                 entity_id=product.get_product_id(),
                                                 attr_value_integer_entity_type=product.get_entity_type(),
                                                 attribute_var=attribute)
                    payload = {
                        'success': True,
                    }

                    break
            else:
                payload = {
                    'success': False,
                    'errors': ['Attribute not found']
                }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload
