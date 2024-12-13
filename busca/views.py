from django.shortcuts import render
from .models import Produto,Fornecedor,Categoria

# Create your views here.

def index(request):
    produto = Produto.objects.all()
    fornecedor = Fornecedor.objects.all()
    categoria = Categoria.objects.all()
    context = {'produtos':produto,'fornecedores':fornecedor,'categorias':categoria}
    return render(request, 'busca/index.html',context)

def details(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'busca/detalhes.html',{'produto':produto})

