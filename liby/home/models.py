from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Models):
	usuario = models.CharField(max_length=20)
	senha = models.CharField(max_length=50)
	email = models.EmailField()
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2)
	foto = models.ImageField()	

class Livro(models.Models):
	ISBN = models.CharField(max_length=20)
	titulo = models.CharField(max_length=20)
	autor = models.CharField(max_length=20)
	edicao = models.CharField(max_length=20)
	dono = models.Foreign(Usuario)

	NOVO = '3'
	BOM = '2'
	RUIM = '1'

	ESTADO_OPCOES = (
		(NOVO,'novo'),
		(BOM,'bom'),
		(RUIM,'ruim')
	)

	estado = models.CharField(max_length=1,opcoes=ESTADO_OPCOES, default=BOM)

class Mensagem(models.Models):
    data = models.DateField(auto_now_add=True)
    conteudo = models.TextField()
    destinatario = models.Foreign(Usuario)	 
    remetente = models.Foreign(Usuario)
    transacao = models.Foreign(Transacao)