from app import app
from flask import render_template, request
from app.models.inventory_managemet_models.CarModels import CarModels
from app.models.inventory_managemet_models.CarCategories import CarCategories
from app.models.Employees import Employees
from app.models.CompletedWork import CompletedWork


@app.route('/add_completed_work', methods=['GET', 'POST'])
def add_completed_work():
    success = False

    if request.method == "POST":
        success = True
        paid_total = int(request.form['paid_total'])
        pay_date = request.form['pay_date']
        description = request.form['description']
        car_model = CarModels.get(car_model_name=request.form['car_models']).first()
        employee = Employees.get(employee_id=request.form['employee_id']).first()

        CompletedWork.create(paid_total=paid_total,
                             pay_date=pay_date,
                             description=description,
                             employee_that_worked=employee,
                             car_model=car_model)

    employees = Employees.get().all()
    car_categories = CarCategories.get()

    return render_template('add_completed_work.html',
                           employees=employees,
                           car_categories=car_categories,
                           success=success)


@app.route('/get_completed_work', methods=["GET"])
def get_completed_work():
    completed_works = CompletedWork.get().all()
    return render_template('completed_works.html', completed_works=completed_works)
