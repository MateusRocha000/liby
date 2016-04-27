from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *

@login_required
def usuarios(request):
	context = {
		'usuarios' : Perfil.objects.all(),
	}

	return render(request, 'usuarios/usuarios.html', context)