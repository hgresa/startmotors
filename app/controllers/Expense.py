from app import app
from flask import render_template, request
from app.models.Expense import Expense


@app.route("/add_expense", methods=["GET", "POST"])
def add_expense():
    success = False
    if request.method == "POST":
        success = True
        paid_total = request.form['paid_total']
        pay_date = request.form['pay_date']
        description = request.form['description']

        Expense.create(paid_total=paid_total,
                       pay_date=pay_date,
                       description=description)

    return render_template('add_expense.html', success=success)


@app.route('/get_expenses', methods=["GET"])
def get_expenses():
    expenses = Expense.get().all()

    return render_template('expenses.html', expenses=expenses)
