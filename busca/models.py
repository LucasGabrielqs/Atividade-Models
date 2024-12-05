from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.CharField(max_length=50,unique=True)
    descricao_produto = models.TextField(max_length=100,blank=True)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    quant_estoque = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
