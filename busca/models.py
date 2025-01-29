from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200,verbose_name="Nome da Catergoria")

    
    def __str__(self):
        return self.nome_categoria

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=250,verbose_name="id do fornecedor")
    cnpj = models.CharField(max_length=14,unique=True) 
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)

    
    def __str__(self):
        return self.nome_fornecedor


class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.CharField(max_length=50,unique=True)
    descricao_produto = models.TextField(max_length=100,blank=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    quant_estoque = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    Categoria = models.ManyToManyField(Categoria,related_name='categorias')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto