from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
]
#As URLs em Django mapeiam as solicitações HTTP para as views correspondentes.
#Este padrão de URL vazia ('') corresponderá à raiz do seu site e chamará a view lista_livros.
