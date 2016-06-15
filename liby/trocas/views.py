from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import *
from datetime import datetime

# Create your views here.
@login_required
def pendentes(request):
	trocas = Troca.objects.filter(perfil_1=request.user.perfil, concluida=False) | Troca.objects.filter(perfil_2=request.user.perfil, concluida=False)
	context = {
		'trocas' : trocas.all().order_by('-data')
	}

	return render(request, 'trocas/pendentes.html', context)

@login_required
def concluidas(request):
	trocas = Troca.objects.filter(perfil_1=request.user.perfil, concluida=True) | Troca.objects.filter(perfil_2=request.user.perfil, concluida=True)
	context = {
		'trocas' : trocas.all().order_by('-data')
	}
	return render(request, 'trocas/concluidas.html', context)



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

@login_required
def nova(request, usuario_id, livro_id):
	p1 = request.user.perfil
	p2 = Perfil.objects.get(user__id=usuario_id)
	l1 = Livro.objects.get(id=livro_id)

	if Troca.objects.filter(perfil_1=p1, perfil_2=p2):
		troca = Troca.objects.filter(perfil_1=p1, perfil_2=p2)[0]
		if not troca.concluida:
			return redirect("/trocas/"+ str(troca.id))

	elif Troca.objects.filter(perfil_1=p2, perfil_2=p1):
		troca = Troca.objects.filter(perfil_1=p2, perfil_2=p1)[0]
		if not troca.concluida:
			return redirect("/trocas/"+str(troca.id))

	else:
		t = Troca()
		t.perfil_1 = p1
		t.perfil_2 = p2
		t.livro_1 = l1
		t.livro_2 = l1
		t.save()
		return redirect('/trocas/' + str(t.id))

@login_required
def selecionar(request, troca_id, livro_id):
	p1 = request.user.perfil
	t = Troca.objects.get(id=troca_id)

	if t.perfil_1 == p1:
		t.livro_1 = Livro.objects.get(id=livro_id)

	if t.perfil_2 == p1:
		t.livro_2 = Livro.objects.get(id=livro_id)

	t.save()			
			
	return redirect('/trocas/' + troca_id)

