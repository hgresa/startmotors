from app import app
from flask import render_template, request, jsonify
from app.models.Salary import Salary
from app.models.Salary import Employees
from ariadne.constants import PLAYGROUND_HTML
from ariadne import graphql_sync
from app.api.queries import resolve_salaries, resolve_salary, resolve_employees, resolve_employee, resolve_expenses, \
    resolve_expense, resolve_monthly_payment_value, resolve_monthly_payment_values, resolve_car_category, \
    resolve_car_categories, resolve_car_model, resolve_monthly_payment_types, resolve_monthly_payment_type
from app.api.mutations import resolve_create_salary, resolve_create_attribute_value, resolve_create_cars, resolve_create_monthly_payment_value
from ariadne import load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers, ObjectType

query = ObjectType('Query')
query.set_field('salary', resolve_salary)
query.set_field('salaries', resolve_salaries)
query.set_field('employees', resolve_employees)
query.set_field('employee', resolve_employee)
query.set_field('expenses', resolve_expenses)
query.set_field('expense', resolve_expense)
query.set_field('monthly_payment_value', resolve_monthly_payment_value)
query.set_field('monthly_payment_values', resolve_monthly_payment_values)
query.set_field('car_category', resolve_car_category)
query.set_field('car_categories', resolve_car_categories)
query.set_field('car_model', resolve_car_model)
query.set_field('monthly_payment_types', resolve_monthly_payment_types)

mutation = ObjectType("Mutation")
mutation.set_field('createSalary', resolve_create_salary)
mutation.set_field('createAttributeValue', resolve_create_attribute_value)
mutation.set_field('createCars', resolve_create_cars)
mutation.set_field('createMonthlyPaymentValue', resolve_create_monthly_payment_value)

# type_defs = load_schema_from_path('/usr/src/app/app/schema.graphql')
# type_defs2 = load_schema_from_path('/usr/src/app/app/models/models.graphql')
type_defs2 = load_schema_from_path('../startmotors/app/models/models.graphql')
type_defs3 = load_schema_from_path('../startmotors/app/models/EAV_models/eav_models.graphql')
type_defs4 = load_schema_from_path('../startmotors/app/models/inventory_managemet_models/'
                                   'inventory_management_models.graphql')
schema = make_executable_schema([type_defs2, type_defs3, type_defs4], query, mutation, snake_case_fallback_resolvers)


@app.route("/salaries", methods=["GET"])
def salaries():
    return render_template("taxes/salaries.html")


@app.route("/add_salary", methods=["GET", "POST"])
def add_salary():
    employees = Employees.get_employees(Employees())
    success = False

    if request.args.get('success'):
        success = True

    return render_template("taxes/add_salary.html", employees=employees, success=success)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
