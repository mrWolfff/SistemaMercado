from django import forms
from .models import Produtos, Venda

class PostForm(forms.ModelForm):

	class Meta:
		model = Produtos
		fields = ('nome', 'descricao', 'quantidade', 'peso', 'valor', 'fornecedor',)

class PostFormVenda(forms.ModelForm):
	class Meta:
		model = Venda
		fields = ('produto_nome', 'produto_descricao', 'produto_quantidade', 'produto_peso', 'produto_valor',)