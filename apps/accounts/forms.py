from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ("nome", "cpf", "telefone", "imagem", )
class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields