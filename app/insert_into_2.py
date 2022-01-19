from app.models import *
from app.models.inventory_managemet_models import *
from app.models.EAV_models import *


products_category_entity = EntityType.create(label="product_categories")
product_entity = EntityType.create(label="product")

products_with_filters = AttributeSet.create(label='products_with_filters')
products_with_litres = AttributeSet.create(label='product_with_litres')
product_basic = AttributeSet.create(label='product_basic')
car_parts = AttributeSet.create(label='car_parts')
oil = AttributeSet.create(label='oil')
hydro_oil = AttributeSet.create(label='hydro_oil')

products_with_filters_arr = ["ზეთის ფილტრები", "ჰაერის ფილტრები", "სალონის ფილტრები", 'ხუნდები']
products_with_litres_arr = ["ანტიფრიზი", "სამუხრუჭე სითხე"]
product_basic_arr = ["საპოხი მასალა", "სახარჯი მასალა", "ნათურები", "გერმეტიკი", "ღვედი", "მანქანის მოვლის საშუალებები", 'დიზელის დანამატი', 'ბენზინის დანამატი']
car_parts_arr = "მანქანის ნაწილები"
oil_arr = "ზეთები"
hydro_oil_arr = "გადაცემათა კოლოფის ზეთები"

for i in products_with_filters_arr:
    product_category = ProductCategories.create(category_name=i,
                                                product_category_entity=products_category_entity,
                                                attribute_set_category=products_with_filters)

for i in products_with_litres_arr:
    product_category_2 = ProductCategories.create(category_name=i,
                                                  product_category_entity=products_category_entity,
                                                  attribute_set_category=products_with_litres)

for i in product_basic_arr:
    product_category_3 = ProductCategories.create(category_name=i,
                                                  product_category_entity=products_category_entity,
                                                  attribute_set_category=product_basic)

product_category_4 = ProductCategories.create(category_name=car_parts_arr,
                                              product_category_entity=products_category_entity,
                                              attribute_set_category=car_parts)

product_category_5 = ProductCategories.create(category_name=oil_arr,
                                              product_category_entity=products_category_entity,
                                              attribute_set_category=oil)

product_category_6 = ProductCategories.create(category_name=hydro_oil_arr,
                                              product_category_entity=products_category_entity,
                                              attribute_set_category=hydro_oil)

integer_data_type  = DataTypes.create(label='integer')
float_data_type    = DataTypes.create(label='float')
varchar_data_type  = DataTypes.create(label='varchar')
datatype_data_type = DataTypes.create(label='datetime')
longtext_data_type = DataTypes.create(label='datetime')

for i in ['sku', 'variety', 'litres_quantity']:
    data_type = varchar_data_type
    if i == 'litres_quantity':
        data_type = integer_data_type

    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=hydro_oil,
                     data_type=data_type)

for i in ['car_countries', 'sku', 'class', 'variety', 'litres_quantity']:
    data_type = varchar_data_type

    if i in ['litres_quantity']:
        data_type = integer_data_type

    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=oil,
                     data_type=data_type)

for i in ['car_model_id', 'sku']:
    data_type = varchar_data_type

    if i == 'car_model_id':
        data_type = integer_data_type

    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=products_with_filters,
                     data_type=data_type)

for i in ['sku', 'variety', 'litres_quantity']:
    data_type = varchar_data_type
    if i == 'litres_quantity':
        data_type = integer_data_type

    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=products_with_litres,
                     data_type=data_type)

for i in ['sku']:
    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=product_basic,
                     data_type=varchar_data_type)

for i in ['car_model_id']:
    Attribute.create(label=i,
                     entity_type=products_category_entity,
                     attribute_set=car_parts,
                     data_type=integer_data_type)

stock_history_group = GroupEntity.create(label='stock_history_group')
order_sales_group = GroupEntity.create(label='order_sales_group')

for i in ['default', 'litres']:
    StockHistoryGroup.create(label=i,
                             group_entity_history=stock_history_group)

    OrderSalesGroup.create(label=i,
                           group_entity_order=order_sales_group)

for i in ['დენი', 'წყალი', 'ინტერნეტი']:
    MonthlyPaymentTypes.create(label=i)
