from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioCreationForm, UsuarioChangeForm
from .models import Usuario, Fornecedor, Cliente

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = [
        "email",
        "username",
        "nome",
        "cpf",
        "telefone",
        "imagem",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("nome", "cpf", "telefone", "imagem",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("nome", "cpf", "telefone", "imagem",)}),)
admin.site.register(Usuario, UsuarioAdmin)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cnpj', 'telefone']
    search_fields = ['nome', 'cnpj']
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email']
    search_fields = ['nome', 'telefone', 'email']