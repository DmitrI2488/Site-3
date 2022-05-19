$(document).on('submit', '#feedback_form', function (e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/feedback_create',
        data: {
            name:$('#name').val(),
            email:$('#email').val(),
            theme:$('#theme').val(),
            message:$('#message').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response){
            console.log('ok - ', response)
            if (response.status === 400) {
                    $('.alert-success').text(response.error).removeClass('d-none');
                    $('#feedback_form')[0].reset();
            }
        },
        error: function (response) {
                console.log('err - ', response)
            }
    })
})