function bootstrapDivElement(classes='')
{
    classes = join(classes)
    return $(`<div class="form-group ${classes}"></div>`)
}

function bootstrapLabelElement(_for, _id="", text="", classes="")
{
    return $(`<label for="${_for}" id="${_id}" class="${join(classes)}">${text}</label>`)
}

export function materialSelect(_id="", name="", classes="")
{
    classes = Array.prototype.join(classes)
    let element = $(`<select id="${_id}" name="${name}" class="${classes}" multiple></select>`)

    return element
}