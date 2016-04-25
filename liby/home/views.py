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
	return render(request, 'home/home.html')

def books(request):
	a = len(Livro.objects.all())
	b = 0
	if a > 10:
		b = a - 10
	context = {
		'livros' : Livro.objects.all()[b::]
	}
	return render(request, 'home/home.html', context)