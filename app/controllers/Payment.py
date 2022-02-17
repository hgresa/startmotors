from app import app
from flask import render_template, request
from app.models.MonthlyPaymentTypes import MonthlyPaymentTypes


@app.route("/get_payments", methods=["GET", "POST"])
def get_payments():

    return render_template('taxes/payments.html')


@app.route("/add_payment", methods=["GET", "POST"])
def add_payment():
    success = False

    if request.args.get('success'):
        success = True

    payment_types = MonthlyPaymentTypes.get()

    return render_template('taxes/add_payment.html', payment_types=payment_types, success=success)
