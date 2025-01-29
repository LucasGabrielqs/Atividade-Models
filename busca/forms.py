from django import forms
from .models import Categoria,Fornecedor,Produto

class ProdutoForms(forms.Form):
    name = forms.CharField(label="nome_produto")
    code = forms.CharField(label="codigo_produto")
    description = forms.CharField(label="descricao_produto")
    price = forms.DecimalField(label="preco_produto")
    amount = forms.IntegerField(label="quant_estoque")
    category = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all())
    supplier = forms.ModelChoiceField(queryset=Fornecedor.objects.all())


class FornecedorForms(forms.Form):
    name = forms.CharField(label="nome_fornecedor")
    cnpj = forms.CharField(label="cnpj")
    rua = forms.CharField(label="rua")
    bairro = forms.CharField(label="bairro")


class CategoriaForms(forms.Form):
    name = forms.CharField(label="nome_categoria")
