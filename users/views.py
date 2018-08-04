from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import FormView

from users.forms import PopeUserForm


class PopeUserFormView(FormView):
    template_name = 'user_form.html'
    form_class = PopeUserForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'dashboard_prestador.html'

    def get_template_name(self):
        if self.request.user.user_type is 'P':
            return 'dashboard_prestador.html'
