from django.shortcuts import render
from django.utils import timezone
from .models import Post, Produto, Venda
from django.shortcuts import redirect
from .forms import PostForm, PostFormVenda
import pdb
def baseRender(request):
	return render(request, 'mercado/base.html')

def produtoRender(request):
	return render(request, 'mercado/produto.html')

def produto(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():	
			form.save()
			return redirect('base.html')
	else:
		form.PostForm()
	return render(request, 'mercado/outro.html', {'form':form} )

def vendaRender(request):
	produto = Produto.objects.all()
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
		produto = Produto.objects.get(id=add)
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
	produtos = Produto.objects.all()
	busca = request.GET.get('pesquisa')
	if busca is not None:
		produtos =  produtos.filter(nome__icontains=busca)
	return render(request, 'mercado/pesquisa_produto.html',{'produtos':produtos})

def pesquisa_produto(request, id):
	produtos = Produto.objects.all()
	busca = request.GET.get('pesquisa')
	if busca is not None:
		produtos =  produtos.filter(nome__icontains=busca)
	return render(request, 'mercado/outro2.html', {'produtos': produtos})



def editarRender(request, id):
	produto = Produto.objects.get(id=id)
	return render(request, 'mercado/editar.html', {'produto': produto})

def editar(request, id):
	produto = Produto.objects.get(id=id)
	form = PostForm(request.POST or None, instance=produto)
	if form.is_valid():
		form.save()
		return redirect('pesquisa_produto.html')
	return render(request, 'mercado/editar2.html', {'form': form, 'produto': produto})

def deletar(request, id):
	produto = Produto.objects.get(id=id)
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