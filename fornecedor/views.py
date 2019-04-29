from django.shortcuts import render
from django.utils import timezone
from .models import Fornecedor
from django.shortcuts import redirect
from .forms import PostFormFornecedor
import pdb

def produtoRender(request):
	return render(request, 'mercado/produto.html')

def cadastroRender(request):
	return render(request, 'fornecedor/cadastro.html')

def cadastro(request):
	if request.method == 'POST':
		form = PostFormFornecedor(request.POST)
		if form.is_valid():	
			form.save()
			return redirect('base.html')
	else:
		form.PostFormFornecedor()
	return render(request, 'fornecedor/outrof.html', {'form':form} )


def fornecedor(request):
	fornecedores = Fornecedor.objects.all()
	busca = request.GET.get('pesquisa')
	if busca is not None:
		fornecedores =  fornecedores.filter(nome__icontains=busca)
	return render(request, 'fornecedor/fornecedor.html',{'fornecedores':fornecedores})


def deletar(request, id):
	fornecedor = Fornecedor.objects.get(id=id)
	if request.method == 'GET':
		fornecedor.delete()
		redirect('fornecedor.html')
	return render(request, 'fornecedor/fornecedor.html', {'fornecedor', fornecedor})
