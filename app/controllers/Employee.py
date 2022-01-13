from app import app
from flask import render_template, request
from app.models import Employees


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    success = False

    if request.method == "POST":
        success = True
        name = request.form["name"]
        surname = request.form["surname"]
        # position = request.form["position"]
        Employees.create(name=name,
                         surname=surname)

    return render_template("add_employee.html", success=success)