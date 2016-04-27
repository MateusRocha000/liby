from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *

@login_required
def livros(request):
	context = {
		'livros' : Livro.objects.all(),
	}

	return render(request, 'livros/livros.html', context)

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
		if request.POST['capa']:
			l.capa = request.POST['capa']
		if request.POST['descricao']:
			l.descricao = request.POST['descricao']
		l.dono = request.user.perfil

		l.save()

		return redirect('/livros/meus-livros/')

	return render(request, 'livros/adicionar.html')

@login_required
def buscar(request):
	if request.method == 'POST':
		titulo = request.POST['titulo']
		autor = request.POST['autor']

		livros = None

		if titulo:
			livros = Livro.objects.filter(titulo__contains=titulo)

		if autor:
			if livros:
				livros &= Livro.objects.filter(autor__contains=autor)
			else:
				livros = Livro.objects.filter(autor__contains=autor)

		context = {
			'livros' : livros
		}

		return render(request, 'livros/buscar.html', context)

	return render(request, 'livros/buscar.html')


@login_required
def livro(request, livro_id):
	context = {
		'livro' : Livro.objects.get(id=livro_id)
	}

	return render(request, 'livros/livro.html', context)
