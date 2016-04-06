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

	NOVO = '***'
	BOM = '**'
	RUIM = '*'

	 ESTADO_OPCOES = (
	 	(NOVO,'novo'),
	 	(BOM,'bom'),
	 	(ruim,'ruim')
	 )

	 estado = models.CharField(max_length=3,opcoes=ESTADO_OPCOES, defaut=BOM)