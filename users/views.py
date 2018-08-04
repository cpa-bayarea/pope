from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from users.forms import PopeUserForm


class PopeUserFormView(FormView):
    template_name = 'user_form.html'
    form_class = PopeUserForm
    success_url = '/login'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.password = make_password(
            form.cleaned_data.get('password')
        )

        new_user.save()

        return super().form_valid(form)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Confirmação de senha não confere com a senha'
            )


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'dashboard_prestador.html'
