from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Livro

def login(request):
	return render(request, 'home/login.html')

@login_required
def logout(request):
	auth_logout(request)
	return redirect('/')

@login_required
def home(request):
	context = {
		'livros' : Livro.objects.all().order_by('-data')[:8]
	}
	return render(request, 'home/home.html', context)

@login_required
def deletarConta(request):
	request.user.delete()
	return redirect('/')

@login_required
def configuracoes(request):
	return render(request, 'home/configuracoes.html')