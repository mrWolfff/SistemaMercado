from django.shortcuts import render
from django.utils import timezone
from .models import Post, Produtos, Venda
from fornecedor.models import Fornecedor
from django.shortcuts import redirect
from .forms import PostForm, PostFormVenda
import pdb
def baseRender(request):
	return render(request, 'mercado/base.html')

def produtoRender(request):
	fornecedor = Fornecedor.objects.all()
	return render(request, 'mercado/produto.html', {'fornecedor':fornecedor})

def produto(request):
	fornecedor = Fornecedor.objects.all()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():	
			form.save()
			return redirect('base.html')
	else:
		form.PostForm()
	return render(request, 'mercado/outro.html', {'form':form, 'fornecedor':fornecedor} )

def vendaRender(request):
	produto = Produtos.objects.all()
	venda = Venda.objects.all()
	valorTotal = 0
	if request.GET.get('fim') is not None:
			venda.delete()
	if request.GET.get('add'):
		add = request.GET.get('add')
		aux = request.GET.get('aux')
		if aux is None:
			aux = 0
		token = request.GET.get('csrfmiddlewaretoken')
		valorTotal = int(aux)
		produto = Produtos.objects.get(id=add)
		valorTotal = valorTotal + int(produto.valor)
		formulario = {'csrfmiddlewaretoken': token,
		'produto_nome': produto.nome,
		'produto_descricao': produto.descricao,
		'produto_quantidade': produto.quantidade,
		'produto_peso': produto.peso,
		'produto_valor': produto.valor}
		form = PostFormVenda(formulario)
		if form.is_valid():
			form.save()
	return render(request, 'mercado/venda.html', {'venda':venda, 'valorTotal': valorTotal})



def pesquisa_produtoRender(request):
	produtos = Produtos.objects.all()
	busca = request.GET.get('pesquisa')
	if busca is not None:
		produtos =  produtos.filter(nome__icontains=busca)
	return render(request, 'mercado/pesquisa_produto.html',{'produtos':produtos})

def pesquisa_produto(request, id):
	produtos = Produtos.objects.all()
	busca = request.GET.get('pesquisa')
	if busca is not None:
		produtos =  produtos.filter(nome__icontains=busca)
	return render(request, 'mercado/outro2.html', {'produtos': produtos})



def editarRender(request, id):
	produto = Produtos.objects.get(id=id)
	fornecedor = Fornecedor.objects.all()
	return render(request, 'mercado/editar.html', {'produto': produto, 'fornecedor':fornecedor})

def editar(request, id):
	produto = Produtos.objects.get(id=id)
	form = PostForm(request.POST or None, instance=produto)
	if form.is_valid():
		form.save()
		return redirect('pesquisa_produto.html')
	return render(request, 'mercado/editar2.html', {'form': form, 'produto': produto})

def deletar(request, id):
	produto = Produtos.objects.get(id=id)
	if request.method == 'POST':
		produto.delete()
		return redirect('pesquisa_produto.html')
	return render(request, 'mercado/deletar.html', {'produto', produto})

def remover(request, id):
	venda = Venda.objects.get(id=id)
	if request.method == 'POST':
		venda.delete()
		return redirect('venda.html')
	return render(request, 'mercado/remover.html', {'produto', produto})