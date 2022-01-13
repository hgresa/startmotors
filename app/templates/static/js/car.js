function on_input() {
    let val = document.getElementById("car_brand").value;
    let opts = document.getElementById('cars').childNodes;
    for (let i = 0; i < opts.length; i++) {
        if (opts[i].value === val) {
            let car_models = get_car_models(opts[i].value)
            appendModelsToSelect('car_models', car_models)
            break;
        }
    }
}

function get_car_categories() {
    $.post({
        async: false,
        url: '/graphql',
        contentType: 'application/json',
        data: JSON.stringify({"query": "{\n" +
                "  car_categories {\n" +
                "    car_categories {\n" +
                "      car_category_id\n" +
                "      car_category_name\n" +
                "      car_models {\n" +
                "        car_model_name\n" +
                "      }\n" +
                "    }\n" +
                "  }\n" +
                "}\n"}),

    }).done(function (response) {

    })
}

function get_car_models(car_category_id) {
        let car_models = []
        $.post({
            async: false,
            url: '/graphql',
            contentType: 'application/json',
            data: JSON.stringify({"query": "{" +
                    `car_category(car_category_id: ${car_category_id}) {\n` +
                    "    car_category {\n" +
                    "      car_models {\n" +
                    "        car_model_name\n" +
                    "        car_model_id\n" +
                    "      }\n" +
                    "    }\n" +
                    "  }" +
                    "}"}),

            }).done(function (response) {
                car_models = response['data']['car_category']['car_category']['car_models']
        })

        return car_models
}

function removeModelsFromSelect(select_element_id) {
    let select_element = $(`#${select_element_id}`)
        select_element.empty()
}

function appendModelsToSelect(select_element_id, car_models) {
    let select_element = $(`#${select_element_id}`)

    removeModelsFromSelect(select_element_id)

    for (const car_model_key in car_models) {
        let car_model = car_models[car_model_key]
        let car_model_id = car_model['car_model_id']
        let car_model_name = car_model['car_model_name']
        let option_element = $(`<option value="${car_model_id}">${car_model_name}</option>`)

        select_element.append(option_element)
    }
}