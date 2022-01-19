// import "./element_builder"

function materialSelect(_id="", name="", classes="")
{
    classes = Array.prototype.join(classes)
    let element = $(`<select id="${_id}" name="${name}" class="${classes}" multiple required></select>`)

    return element
}

function renderCarDom(attribute_name)
{
    let form_element = $('#the_form')

    let car_categories_id = $("select[id*='car_categories']").length
    let car_models_id = $("select[id*='car_models']").length
    let car_models_div_id = $("div[id*='car_wrapper_div']").length

    $.ajax({
        url: "/get_car_categories",
        type: "post",
        success: function( car_categories ) {
            let bootstrap_div_element = $('<div class="form-group" style="border: 2px solid; padding: 5px"></div>')
            let bootstrap_label_element = $(`<label for="car_categories-${car_categories_id}" class="form-label">მანქანის კატეგორია</label>`)
            let bootstrap_select_element = $(`<select onchange="displayCarModels(this)" class="form-control" id="car_categories-${car_categories_id}" name="car_categories-${car_categories_id}" required>`)
                bootstrap_select_element.append('<option></option>')

            for (const index in car_categories) {
                let car_category_name = car_categories[index]
                let option_element = $(`<option value="${car_category_name}">${car_category_name}</option>`)

                bootstrap_select_element.append(option_element)
            }

            bootstrap_div_element.append(bootstrap_label_element)
            bootstrap_div_element.append(bootstrap_select_element)

            let car_models_div = $(
                `    <div id="car_wrapper_div-${car_models_div_id}" class="form-group">\n` +
                `        <label for="car_models-${car_models_id}" class="form-label">მანქანის მოდელი</label>\n` +
                '    </div>')
            let car_models_select = materialSelect(`car_models-${car_models_id}`, attribute_name, ['form-control'])
                car_models_div.append(car_models_select)

            bootstrap_div_element.append(car_models_div)
            form_element.append(bootstrap_div_element)
            form_element.append($('#submit'))
          }
    })
}

function displayCarModels(element)
{
    let identifier = element.id.match(/.*-(.*)/)[1]
    let car_model_select_element = $(`#car_models-${identifier}`)
        car_model_select_element.empty()
    let car_model_div_element = $(`#car_wrapper_div-${identifier}`)
        if (car_model_div_element.length) {
            let parent_form_group = car_model_div_element.parent()
            car_model_div_element.remove()

            let car_model_wrapper = $(`<div id="car_wrapper_div-${identifier}" class="form-group"></div>`)
            let label = $(`<label class="form-label" for="car_models-${identifier}">მანქანის მოდელი></labelმანქანის>`)
            let car_model_select = materialSelect(`car_models-${identifier}`)
            car_model_wrapper.append(label)
            car_model_wrapper.append(car_model_select)
            parent_form_group.append(car_model_wrapper)
        }

    car_model_select_element = $(`#car_models-${identifier}`)

    $.ajax({
        url: "/get_car_models",
        type: "post",
        data: {
            car_category_name: element.value
          },
        success: function( result ) {
            for (const resultKey in result) {
                let car_model = result[resultKey]
                car_model_select_element.append(`<option value="${car_model}">${car_model}</option>`)
            }

            if (window.location.pathname !== '/add_completed_work') {
                let multipleCancelButton = new Choices(`#car_models-${identifier}`, {
                removeItemButton: true
            })
            }
          }
    })
}

function appendPaymentTypes()
{
    let payments_table_wrapper = $('#payments_table_wrapper')
    let payment_type_select_element = $('#payments_form')

    let checkExistence = setInterval(function() {
        if (payments_table_wrapper.length) {
            payments_table_wrapper.append(payment_type_select_element)
        }
        clearInterval(checkExistence);
    }, 100)
}

function getAttributes(product_category)
{
        let form_element = $('#the_form')
            form_element.children().not(':nth-child(-n+5)').remove()

        $.ajax({
            url: "/get_attributes",
                async: false,
            type: "post",
            data: {
                product_category: product_category
              },
            success: function( result ) {
                for (const key in result) {
                    let attribute_name = result[key]
                    let translation = {"litres_quantity": "ლიტრა", 'car_model_id': 'მანქანის მოდელი', 'sku': 'კოდი', 'variety': 'სახეობა',
                                        'class': 'კლასი', 'car_countries': 'მანქანის ქვეყნები'}

                    if (attribute_name === "car_model_id") {
                        renderCarDom(attribute_name)
                    }
                    else {
                        let bootstrap_label_element = $(`<label for="${attribute_name}" class="form-label">${attribute_name}</label>`)

                        if (attribute_name in translation) {
                            bootstrap_label_element = $(`<label for="${attribute_name}" class="form-label">${translation[attribute_name]}</label>`)
                        }

                        let bootstrap_input_element = $(`<input type="text" class="form-control" name="${attribute_name}" id="${attribute_name}" aria-describedby="${attribute_name}" required>`)
                        let bootstrap_div_element = $('<div class="form-group"</div>')
                            bootstrap_div_element.append(bootstrap_label_element)
                            bootstrap_div_element.append(bootstrap_input_element)

                        form_element.append(bootstrap_div_element)
                    }
                }
                let submit_button = '<button onclick="test(event)" class="btn btn-primary" id="submit" type="submit">დამატება</button>'
                form_element.append(submit_button)
                if (result.includes("car_model_id")) {
                    $('#submit').before(`<button onclick="renderCarDom('car_model_id')" id="add_car" type="button" class="btn btn-success">+</button>`)
                }
              }
        })
}

function test(event) {
    let form_element = $('#the_form')
    event.preventDefault()

    if($('form#the_form').validate().form())
    {
        let car_models_count = $("select[id*='car_models']").length
        let car_wrapper_div_count = $("div[id*='car_wrapper_div']").length

        for (let i = 0; i < car_models_count; i++) {
            $(`#car_models-${i}`).remove()
        }

        let form_data = $('form').serializeArray()

        let car_models = []
        for (let i = 0; i < car_wrapper_div_count; i++) {
            let elem = $(`#car_wrapper_div-${i}`).children().last().children().first().children().first().children()
            for (let j = 0; j < elem.length; j++) {
                let item = elem[j]
                let value = item.getAttribute('data-value')
                car_models.push(value)
            }
        }

        $.ajax({
            url: "/add_product",
            type: "post",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            data: {
                form: JSON.stringify(form_element.serializeArray()), car_model_id: JSON.stringify(car_models)
              },
            success: function () {
                window.location.search += '&success=1';
            }
        })
    }
    else
    {

    }
}
