from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Livro

@login_required
def livros(request):
	return render(request, 'livros/livros.html')

@login_required
def meusLivros(request):
	context = {
		'livros' : Livro.objects.filter(dono=request.user.perfil)
	}
	return render(request, 'livros/meus-livros.html', context)

@login_required
def adicionar(request):

	if request.method == 'POST':
		l = Livro()
		l.titulo = request.POST['titulo']
		l.autor = request.POST['autor']
		l.capa = request.POST['capa']
		l.descricao = request.POST['descricao']
		l.dono = request.user.perfil

		l.save()

		return redirect('/livros/meus-livros/')

	return render(request, 'livros/adicionar.html')