// $(document).ready( function () {
//     let datatable = $('#table_id').dataTable({searching: false});
// });
let datatable = $('#table_id').DataTable({
        "order": [],
         "language": {
             "search": "ძებნა:",
             "emptyTable": "ჩანაწერები არ მოიძებნა",
             "paginate": {
                 "next": "წინ",
                 "previous": 'უკან'
             }
         }
})

function init(product_categories)
{
    displayCategoryList(product_categories)
}

function displayCategoryList(product_categories)
{
        let checkExist = setInterval(function() {
        if ($('#table_id_wrapper').length) {
            // let first_element = $('#table_id_wrapper').children(':first')
            let bootstrap_form_element = $('<form id="category_form" action="" method="post"></form>')
            let bootstrap_div_element = $('<div class="row col-sm-12 col-md-6"</div>')
            let bootstrap_label_element = $('<label for="product_category" class="col-sm-2 col-form-label col-form-label-sm">კატეგორია</label>')
            let bootstrap_col_div_element = $('<div class="col-sm-10"></div>')
            let bootstrap_select_element = $('<select class="form-control form-control-sm" id="product_category" name="product_category"></select>')

            for (const index in product_categories) {
                let product_category_name = product_categories[index]
                bootstrap_select_element.append(`<option value="${product_category_name}">${product_category_name}</option>`)
            }

            bootstrap_col_div_element.append(bootstrap_select_element)
            bootstrap_div_element.append(bootstrap_label_element)
            bootstrap_div_element.append(bootstrap_col_div_element)
            bootstrap_form_element.append(bootstrap_div_element)
            bootstrap_form_element.append('<button class="btn btn-primary">მიღება</button>')
            $('#table_id_wrapper').append(bootstrap_form_element)
            clearInterval(checkExist);
            $('#product_category').val(saved_category)
        }
        }, 100);
}


// function changeTableData(product_category_name)
// {
//     let table_body = $('#table_body')
//         table_body.empty()
//
//         $.ajax({
//             url: "/get_products",
//             type: "post",
//             data: {
//                 product_category_name: product_category_name
//             },
//             success: function (product) {
//                 console.log(product)
//                 let attribute_entities = product['attribute_entities']
//                 let titles = product['titles']
//
//                 let titles_tr_element = $("#titles")
//                     titles_tr_element.children().not(':nth-child(-n+4)').remove()
//
//                 for (const titlesElementKey in titles) {
//                     let title = titles[titlesElementKey]
//
//                     titles_tr_element.append(`<th>${title}</th>`)
//                 }
//
//                 for (const index in attribute_entities) {
//                     let tr_element = $('<tr></tr>')
//
//                     let entity_arr = attribute_entities[index]
//                     let product_name = entity_arr['product_name']
//                     let product_id = entity_arr['product_id']
//                     let stock = entity_arr['stock']
//                     let price_per_piece = entity_arr['price_per_piece']
//                     // tr_element.append(
//                     //     `<td>${product_name}</td>` +
//                     //     `<td>${product_id}</td>` +
//                     //     `<td>${stock}</td>` +
//                     //     `<td>${price_per_piece}</td>`
//                     // )
//                     datatable.rows.add(["1", "2", "3", "4"])
//                     for (let key in entity_arr) {
//                         if (!['product_id', 'stock', 'price_per_piece', 'product_name'].includes(key)) {
//                         //     let value = entity_arr[key]
//                         //     let td_element = $(`<td>${value}</td>`)
//
//                             // tr_element.append(td_element)
//                         }
//
//                     }
//                     // table_body.append(tr_element)
//                 }
//             }
//         })
// }