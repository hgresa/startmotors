class Salary {
    get_salary(salary_id) {

    }

    get_salaries() {
        let salaries = []
        $.post({
            async: false,
            url: '/graphql',
            contentType: 'application/json',
            data: JSON.stringify({
                query: '{' +
                    'salaries {' +
                        'success,' +
                        'errors,' +
                        'salaries {' +
                                'salary_id,' +
                                'amount,' +
                                'pay_date,' +
                                'created_at,' +
                                'employee {' +
                                    'name,' +
                                    'surname' +
                                '}' +
                            '}' +
                        '}' +
                    '}'})
            }).done(function (response) {
                salaries = response['data']['salaries']['salaries']
        })

        return salaries
    }

    create_salary(amount, pay_date, employee_id) {
        $.post({
            async: false,
            url: '/graphql',
            contentType: 'application/json',
            data: JSON.stringify({
                query: 'mutation createSalary {' +
                    'createSalary(' +
                        `amount: ${amount},` +
                        `pay_date: "${pay_date}",` +
                        `employee_id: ${employee_id}` +
                    ') {' +
                            'success,' +
                            'errors,' +
                        '}' +
                    '}'
            })
        }).done(function (response) {
            if (response['data']['createSalary']['success'] === true) {
                window.location.search += 'success=true';
            }
        })
    }

    populateDataTable() {
        let salaries = this.get_salaries()
        let data_table = $('#table_id').DataTable()

        data_table.clear();
        for (const salaryKey in salaries) {
            let salary = salaries[salaryKey]
            let salary_id = salary['salary_id']
            let amount = salary['amount']
            let created_at = salary['created_at']
            let pay_date = salary['pay_date']
            let employee = salary['employee']
            let employee_name = employee['name']
            let employee_surname = employee['surname']

            data_table.rows.add([
                {
                    0: employee_name,
                    1: employee_surname,
                    2: amount,
                    3: pay_date,
                    4: created_at
                }
            ])
        }
        data_table.draw();
    }

    handle_salary_save() {
        let form_data = $('#the_form').serializeArray()
        let amount = form_data[1].value
        let pay_date = form_data[2].value
        let employee_id = form_data[0].value

        this.create_salary(amount, pay_date, employee_id)
    }
}
