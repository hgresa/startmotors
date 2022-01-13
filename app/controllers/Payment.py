from app import app
from flask import render_template, request
from app.models.MonthlyPaymentTypes import MonthlyPaymentTypes
from app.models.MonthlyPaymentValue import MonthlyPaymentValue


@app.route("/get_payments", methods=["GET", "POST"])
def get_payments():
    payment_types = MonthlyPaymentTypes.get()
    payments_arr = MonthlyPaymentValue.get_fully_qualified_values(MonthlyPaymentValue())

    # if request.args.get('payment_type'):
    #     payments_arr = MonthlyPaymentValue.get_fully_qualified_values(MonthlyPaymentValue())
    #
    #     return render_template('taxes/payments.html', payment_types=payment_types, payments_arr=payments_arr)

    return render_template('taxes/payments.html', payment_types=payment_types, payments_arr=payments_arr)
    # return render_template("taxes/payments.html", payment_types=payment_types)


@app.route("/add_payment", methods=["GET", "POST"])
def add_payment():
    success = False

    if request.method == "POST":
        success = True
        amount = request.form["amount"]
        pay_date = request.form["pay_date"]
        payment_type = MonthlyPaymentTypes.get(label=request.form["payment_type"]).first()
        MonthlyPaymentValue.create(value=amount,
                                   pay_date=pay_date,
                                   payment_type=payment_type)

    payment_types = MonthlyPaymentTypes.get()

    return render_template('taxes/add_payment.html', payment_types=payment_types, success=success)
