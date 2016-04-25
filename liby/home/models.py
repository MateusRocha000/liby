from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nome  = models.CharField(max_length=100)
	foto  = models.CharField(max_length=100)
	cidade = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Livro(models.Model):
	ISBN = models.CharField(max_length=20)
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=100)
	capa  = models.CharField(max_length=100)
	edicao = models.CharField(max_length=20)
	data = models.DateField(auto_now_add=True)
	descricao = models.TextField()
	dono = models.ForeignKey(Perfil)	

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
		return self.titulo + ' by ' + self.autor

class Transacao(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
	usuarioSolicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	concluida = models.BooleanField(default=False)
	avaliacaoDono = models.TextField()
	avaliacaoSolicitante = models.TextField()
	notaDono = models.IntegerField()
	notaSolicitante = models.IntegerField()

class Mensagem(models.Model):
	data = models.DateField(auto_now_add=True)
	conteudo = models.TextField()
	destinatario = models.ForeignKey(Perfil, related_name='destinatario')
	remetente = models.ForeignKey(Perfil, related_name='remetente')
	transacao = models.ForeignKey(Transacao)

	def __str__(self):
		return self.conteudo
