from django.views.generic.edit import FormView

from organizations.forms import PopeOrganizationForm


class PopeOrganizationFormview(FormView):
    template_name = 'organization_form.html'
    form_class = PopeOrganizationForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
