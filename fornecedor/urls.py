from django.urls import path
from  . import views

urlpatterns = [
path('fornecedor/', views.fornecedor, name='fornecedor.html'),
path('cadastro/', views.cadastroRender, name='cadastro.html'),
path('cadastroFim/', views.cadastro, name='outrof.html'),
path('deletarf/<int:id>', views.deletar, name='deletarf.html'),
]