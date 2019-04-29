from django import forms
from .models import Fornecedor

class PostFormFornecedor(forms.ModelForm):

	class Meta:
		model = Fornecedor
		fields = ('nome', )
