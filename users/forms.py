"""Classes for forms related to users."""
from django.forms import ModelForm

from users.models import User


class PopeUserForm(ModelForm):
    """Form for ordinary users."""
    class Meta:
        """Meta default."""
        model = User
        fields = ['username', 'password', 'email', 'user_type']
