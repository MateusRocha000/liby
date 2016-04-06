from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
	usuario = models.CharField(max_length=20)
	senha = models.CharField(max_length=50)
	email = models.EmailField()
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=2)
	foto = models.CharField(max_length=100)

	def __str__(self):
		return self.usuario

class Livro(models.Model):
	ISBN = models.CharField(max_length=20)
	titulo = models.CharField(max_length=20)
	autor = models.CharField(max_length=20)
	edicao = models.CharField(max_length=20)
	dono = models.ForeignKey(Usuario)

	NOVO = '3'
	BOM = '2'
	RUIM = '1'

	ESTADO_OPCOES = (
		(NOVO,'novo'),
		(BOM,'bom'),
		(RUIM,'ruim')
	)

	estado = models.CharField(max_length=1, choices=ESTADO_OPCOES, default=BOM)

	def __str__(self):
		return self.titulo

class Transacao(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	usuarioSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	concluida = models.BooleanField(default=False)
	avaliacaoDono = models.TextField()
	avaliacaoSolicitante = models.TextField()
	notaDono = models.IntegerField()
	notaSolicitante = models.IntegerField()

class Mensagem(models.Model):
	data = models.DateField(auto_now_add=True)
	conteudo = models.TextField()
	destinatario = models.ForeignKey(Usuario, related_name='destinatario')
	remetente = models.ForeignKey(Usuario, related_name='remetente')
	transacao = models.ForeignKey(Transacao)

	def __str__(self):
		return self.conteudo