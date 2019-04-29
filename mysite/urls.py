
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mercado.urls',)),
    path('', include('fornecedor.urls',)),
]