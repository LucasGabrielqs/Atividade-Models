from django.contrib import admin
from .models import Produto,Fornecedor,Categoria
# Register your models here.



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_produto','nome_produto','preco_produto','quant_estoque','data_criacao']
    search_fields = ['codigo_produto','nome_produto']
    list_filter = ['data_criacao']
    ordering = ['-data_criacao']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
