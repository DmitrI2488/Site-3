from members.forms import RegistrationAjaxForm


def get_context_data(request):
    context = {
        'register_ajax': RegistrationAjaxForm()
    }
    return context
