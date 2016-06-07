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
	saulo = request.user.perfil
	lucas = Perfil.objects.get(nome__contains='Lucas R')


	m1 = Mensagem(remetente=saulo, 
				  destinatario=lucas,
				  conteudo="Ola Lucão, como está?",
				  data=datetime.now())
	m2 = Mensagem(remetente=lucas,
				  destinatario=saulo,
				  conteudo="Bem.",
				  data=datetime.now())

	m3 = Mensagem(remetente=saulo, 
				  destinatario=lucas,
				  conteudo="Vamos trocar o livrin?",
				  data=datetime.now())
	m4 = Mensagem(remetente=lucas,
				  destinatario=saulo,
				  conteudo="#partiu",
				  data=datetime.now())

	context = {
		'mensagens' : [m1, m2, m3, m4, m4, m3],
		'destinatario' : saulo,
		'remetente' : lucas,
		'trocaRealizada' : True
	}
	return render(request, 'trocas/troca.html', context)