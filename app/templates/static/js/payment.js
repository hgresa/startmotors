class Payment {
    get_payment() {

    }

    get_payment_types() {

    }

    get_payments() {
        let payments = [];
        $.post({
            async: false,
            url: '/graphql',
            contentType: 'application/json',
            data: JSON.stringify({
                query: '{' +
                    'monthly_payment_values {' +
                            'success,' +
                            'errors,' +
                            'monthly_payment_values {' +
                                'pay_date,' +
                                'payment_id,' +
                                'created_at,' +
                                'value,' +
                                'type {' +
                                    'label' +
                                '}' +
                            '}' +
                        '}' +
                    '}'
            })
        }).done(function (response) {
            payments = response['data']['monthly_payment_values']['monthly_payment_values'];
        })

        return payments;
    }

    create_payment(amount, pay_date, payment_type) {
        $.post({
            async: false,
            url: '/graphql',
            contentType: 'application/json',
            data: JSON.stringify({
                query: "mutation createPayment {" +
                    "createMonthlyPaymentValue(" +
                        `amount: ${amount},` +
                        `pay_date: "${pay_date}", ` +
                        `payment_type: "${payment_type}"` +
                    ") {" +
                        "success " +
                        "errors " +
                        "monthly_payment_value {" +
                            "payment_id," +
                            "type {" +
                                "label" +
                            "}, " +
                            "value, " +
                            "pay_date" +
                            "}" +
                        "}" +
                    "}",
            })
        }).done(function (response) {
            if (response['data']['createMonthlyPaymentValue']['success'] === 'true') {
                window.location.search += 'success=true';
            }
        })
    }

    populate_data_table() {
        let payments = this.get_payments()
        let data_table = $('#payments_table').DataTable()

        data_table.clear()

        for (const paymentKey in payments) {
            let payment = payments[paymentKey]
            let type = payment['type']
            let payment_label = type['label']
            let payment_id = payment['payment_id']
            let value = payment['value']
            let pay_date = payment['pay_date']
            let created_at = payment['created_at']

            data_table.rows.add([
                {
                    0: payment_label,
                    1: value,
                    2: pay_date,
                    3: created_at
                }
            ])
        }

        data_table.draw()

    }

    handlePaymentSave() {
        let form_data = $('#the_form').serializeArray()
        let payment_type = form_data[0].value
        let amount = form_data[1].value
        let pay_date = form_data[2].value

        this.create_payment(amount, pay_date, payment_type)
    }
}