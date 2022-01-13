from app import app
from flask import render_template, request
from app.models.Salary import *


@app.route("/get_salary_statistics")
def get_salary_statistics():
    from_date = request.args.get('from')
    to_date = request.args.get('to')
    salary_obj = Salary.get_instance()
    salary_list = salary_obj.get_salary_sum('2021-10-01', '2021-10-31')

    return f"<h1>{request.args}</h1>"
