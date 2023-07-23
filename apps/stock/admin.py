from django.contrib import admin
from .models import Categoria, Produto, Venda

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'quantidade_estoque', 'categoria']
    search_fields = ['nome', 'categoria__nome']
    
@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'produto', 'quantidade', 'preco', 'forma_pagamento', 'parcelamento']
    search_fields = ['cliente__nome', 'produto__nome']
