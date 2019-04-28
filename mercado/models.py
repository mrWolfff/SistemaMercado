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

class Produto(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    quantidade = models.CharField(max_length=10)
    peso = models.CharField(max_length=10)
    valor = models.CharField(max_length=10)


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

class VendasRealizadas(models.Model):
    venda_id = models.CharField(max_length=200)

    def valorTotal(self):
        valor = 0
        vendas = Venda.objects.all().filter(nota=self)
        for v in vendas:
            valor += (v.produto_valor * v.produto_quantidade)
        return valor
