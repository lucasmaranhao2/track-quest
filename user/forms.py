from .models import RegisterModel
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = RegisterModel
        fields = ['username', 'email']