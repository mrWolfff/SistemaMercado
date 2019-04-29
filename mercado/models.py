from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

        def __str__(self):
            return self.title

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    quantidade = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=100, default='SOME STRING')


    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto_nome = models.CharField(max_length=200)
    produto_descricao = models.CharField(max_length=200)
    produto_quantidade = models.CharField(max_length=200)
    produto_peso = models.CharField(max_length=200)
    produto_valor = models.CharField(max_length=200)

    def __str__(self):
        return self.produto_nome

    def valorTotal(self):
        valor = 0
        vendas = Venda.objects.all().filter(nota=self)
        for v in vendas:
            valor += (v.produto_valor * v.produto_quantidade)
        return valor

    