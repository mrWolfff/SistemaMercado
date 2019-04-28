from django import forms
from .models import Produto, Venda

class PostForm(forms.ModelForm):

	class Meta:
		model = Produto
		fields = ('codigo', 'nome', 'descricao', 'quantidade', 'peso', 'valor',)

class PostFormVenda(forms.ModelForm):
	class Meta:
		model = Venda
		fields = ('produto_nome', 'produto_descricao', 'produto_quantidade', 'produto_peso', 'produto_valor',)