let product_id = 0
let litres = $('#litres_quantity')
let modal_submit_button = $('#modal_submit_button')

$('#sale_modal').on('shown.bs.modal', function (element) {
    product_id = $(element.relatedTarget)

    if (litres.length) {
        if (!$('#litres_qty').length) {
                    $('#modal_body').append(
            '                    <div class="form-group">\n' +
            '                        <label for="litres_qty" class="form-label">ლიტრის რაოდენობა</label>\n' +
            '                        <input type="text" class="form-control" name="litres_qty" id="litres_qty" aria-describedby="litres_qty">\n' +
            '                    </div>'
                    )
        }

        $('#quantity_div').hide()
    }
})

function configureModal(option)
{
    if (option === "sell") {
        modal_submit_button.attr('onclick', 'sell()')
        $('#exampleModalLabel').text('გაყიდვა')
    } else if (option === "buy") {
        modal_submit_button.attr('onclick', 'buy()')
        $('#exampleModalLabel').text('ყიდვა')
    }
}

function sell()
{
    let quantity = $('#quantity').val()
    let price_per_piece = $('#price_per_piece').val()
    let data = {"product_id": product_id.attr('value'), "quantity": quantity, "price_per_piece": price_per_piece}

    if (litres.length) {
        data["litres"] = $('#litres_qty').val()
        data['quantity'] = 1
    }

    $.ajax({
        url: "/sell_product",
        type: "post",
        data: data,
        success: function (response) {
            if (response['code'] === "SUCCESS") {
                $('#category_form').submit()
                // let tr_element = product_id.parent().parent()
                // let qty_td_element = tr_element.children().eq(2)
                //     qty_td_element.text(Number(qty_td_element.text()) - Number(quantity))
            }
        },
        error: function (response) {

        }
    })
}

function buy()
{
    let quantity = $('#quantity').val()
    let price_per_piece = $('#price_per_piece').val()
    let data = {"product_id": product_id.attr('value'), "quantity": quantity, "price_per_piece": price_per_piece}

    if (litres.length) {
        data["litres"] = $('#litres_qty').val()
        data['quantity'] = 1
    }

    $.ajax({
        url: "/buy_product",
        type: "post",
        data: data,
        success: function (response) {
            $('#category_form').submit()
        },
        error: function (response) {

        }
    })
}