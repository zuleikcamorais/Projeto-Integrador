from django.shortcuts import render

from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})

# Create your views here.
#As views são funções ou classes em Django que aceitam solicitações HTTP e retornam respostas HTTP. 
#Edite o arquivo livros/views.py para definir as views necessárias para a sua aplicação.
 
#Esta é uma view simples que consulta todos os livros do banco de dados e passa esses livros para um template chamado lista_livros.html.
