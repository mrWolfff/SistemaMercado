from django.urls import path
from  . import views

urlpatterns = [
path('', views.baseRender, name='base.html'),
path('produto/', views.produtoRender, name='produto.html'),
path('venda/', views.vendaRender, name='venda.html'),
path('outro/', views.produto, name='outro.html'),
path('pesquisas/', views.pesquisa_produtoRender, name='pesquisa_produto.html'),
path('pesquisas/', views.pesquisa_produto, name='outro2.html'),
path('editar/<int:id>/', views.editarRender, name='editar.html'),
path('editar2/<int:id>/', views.editar, name='editar2.html'),
path('deletar/<int:id>/', views.deletar, name='deletar.html'),
path('remover/<int:id>/', views.remover, name='remover.html'),
]