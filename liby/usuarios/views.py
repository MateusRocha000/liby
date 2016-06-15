from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *
from .controllers import *

@login_required
def usuarios(request):
	context = {
		'usuarios' : Perfil.objects.all(),
	}

	return render(request, 'usuarios/usuarios.html', context)

@login_required
def buscar(request):
	if request.method == 'POST':
		context = {
			'nome' : request.POST['nome'],
			'usuarios' : buscarUsuario(request.POST['nome']),
			'buscaRealizada' : True,
		}
		return render(request, 'usuarios/buscar.html', context)

	else:
		return render(request, 'usuarios/buscar.html')

@login_required
def usuario(request, usuario_id):
	context = {
		'usuario' : Perfil.objects.get(id=usuario_id),
	}

	return render(request, 'usuarios/usuario.html', context)

@login_required
def seguindo(request):
	return render(request, 'usuarios/seguindo.html')

@login_required
def seguidores(request):
	return render(request, 'usuarios/seguidores.html')

@login_required
def seguir(request, usuario_id):
	perfil = Perfil.objects.get(id=usuario_id)
	request.user.perfil.seguindo.add(perfil)

	return redirect("/usuarios/" + usuario_id)


@login_required
def deixardeseguir(request, usuario_id):
	perfil = Perfil.objects.get(id=usuario_id)
	request.user.perfil.seguindo.remove(perfil)

	return redirect("/usuarios/" + usuario_id)

