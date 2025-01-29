from django.shortcuts import render
from .models import Produto,Fornecedor,Categoria
from .forms import CategoriaForms,FornecedorForms,ProdutoForms
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.

# def index(request):
#     produto = Produto.objects.all()
#     fornecedor = Fornecedor.objects.all()
#     categoria = Categoria.objects.all()
#     context = {'produtos':produto,'fornecedores':fornecedor,'categorias':categoria}
#     return render(request, 'busca/index.html',context)

# def details(request,id):
#     produto = Produto.objects.get(id=id)
#     return render(request,'busca/detalhes.html',{'produto':produto})



def Index(request):
    return render(request, 'busca/index.html')

def Lista(request, choice):
    if choice == 'produtos':
        produtos = Produto.objects.all()
        context = {'produtos':produtos}

    elif choice == 'fornecedores':
        fornecedores = Fornecedor.objects.all()
        context = {'fornecedores':fornecedores}

    elif choice == 'categorias':
        categorias = Categoria.objects.all()
        context = {'categorias':categorias}

    return render(request, 'busca/table.html', context)

def DetailProduct(request, pk):
    produto = Produto.objects.get(id=pk)
    context = {'produto': produto}
    return render(request, 'busca/detalhes.html', context)

def create_product(request):
    if request.method =="POST":
        form = ProdutoForms(request.POST)
        if form.is_valid():
            produto = Produto(
                nome_produto=form.cleaned_data['name'],
                codigo_produto=form.cleaned_data['code'],
                descricao_produto=form.cleaned_data.get('description'),  
                preco_produto=form.cleaned_data['price'],
                quant_estoque=form.cleaned_data['amount'],
                fornecedor=form.cleaned_data['supplier']
            )
            produto.save()
            produto.Categoria.set(form.cleaned_data['category'])
            return redirect('listing', 'categorias')
    else:
        form = ProdutoForms()
        return render(request, "busca/forms/formulario_produto.html", {'form':form})
    
def create_supplier(request):
    if request.method =="POST":
        form = FornecedorForms(request.POST)
        if form.is_valid():
            supplier = Fornecedor(
                nome_fornecedor = form.cleaned_data['name'],
                cnpj = form.cleaned_data['cnpj'],
                rua = form.cleaned_data['rua'],
                bairro = form.cleaned_data['bairro'],
            )
            supplier.save()
            return redirect('listing', 'fornecedores')
    else:
        form = FornecedorForms()
        return render(request, "busca/forms/formulario_fornecedor.html", {'form':form})
    

def create_category(request):
    if request.method == "POST":
        form = CategoriaForms(request.POST)
        if form.is_valid():
            category = Categoria(
                nome_categoria = form.cleaned_data['name'],
            )
            category.save()
            return redirect('listing', 'categorias')
    else:
        form = CategoriaForms()
        return render(request, "busca/forms/formulario-categoria.html", {'form':form})