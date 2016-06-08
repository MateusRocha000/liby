from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *
from datetime import datetime

# Create your views here.
@login_required
def trocas(request):
	context = {
		'trocas' : Troca.objects.filter(perfil_1=request.user.perfil) | Troca.objects.filter(perfil_2=request.user.perfil)
	}
	return render(request, 'trocas/trocas.html', context)

@login_required
def troca(request, troca_id):
	context = {
		"troca" : Troca.objects.get(id=troca_id),
		"mensagens" : Mensagem.objects.filter(troca__id=troca_id)
	}

	return render(request, 'trocas/troca.html', context)

@login_required
def mensagem(request, troca_id):
	m = Mensagem()
	m.remetente = request.user.perfil
	m.troca = Troca.objects.get(id=troca_id)
	m.conteudo = request.POST['conteudo']
	m.save()

	return redirect('/trocas/' + troca_id)
