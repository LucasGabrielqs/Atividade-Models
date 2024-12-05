from django.contrib import admin
from .models import Produto
# Register your models here.



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo_produto','nome_produto','preco_produto','quant_estoque','data_criacao']
    search_fields = ['codigo_produto','nome_produto']
    list_filter = ['data_criacao']
    ordering = ['-data_criacao']


admin.site.register(Produto, ProdutoAdmin)