from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ChoiceField

class FormularioRegistro(UserCreationForm):
    grupo = ChoiceField(required=True, choices=(
        ("Usuario Común", "Usuario Común"),
        ("Moderador", "Moderador")
    ))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("grupo", "first_name", "last_name", "email")
