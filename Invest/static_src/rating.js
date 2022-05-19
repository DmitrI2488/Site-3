function AjaxPagination() {
    $('#pagination a.page-link').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            console.log(page_url)

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('#posts').empty()
                    $('#posts').append( $(data).find('#posts').html() )
                    console.log($(data).find('#posts').html())

                    $('#pagination').empty()
                    $('#pagination').append($(data).find('#pagination').html())
                    console.log($(data).find('#pagination').html())
                }
            })
        })
    })
}

$(document).ready(function() {
    AjaxPagination()
})

$(document).ajaxStop(function() {
    AjaxPagination()
})