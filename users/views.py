from django.views.generic.edit import FormView

from users.forms import PopeUserForm


class PopeUserFormView(FormView):
    template_name = 'user_form.html'
    form_class = PopeUserForm
    success_url = '/login'
