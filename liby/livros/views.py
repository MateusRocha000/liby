from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def livros(request):
	return render(request, 'livros/livros.html')

@login_required
def meusLivros(request):
	return render(request, 'livros/meus-livros.html')

@login_required
def adicionar(request):
	return render(request, 'livros/adicionar.html')