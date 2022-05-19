var loading=false;
$(window).scroll(function(){
    if (!loading && ($(window).scrollTop() > $(document).height()-$(window).height-100)){
        loading=true;
        $.ajax({
            type: 'GET',
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
        }
})