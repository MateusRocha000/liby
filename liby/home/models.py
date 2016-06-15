from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nome  = models.CharField(max_length=100)
	foto  = models.CharField(max_length=100)
	cidade = models.CharField(max_length=50)
	seguindo = models.ManyToManyField("self", related_name='seguidores')

	def __str__(self):
		return self.nome

	def meusLivros(self):
		return self.livros.all()

class Livro(models.Model):
	titulo = models.CharField(max_length=100)
	autor = models.CharField(max_length=100)
	capa  = models.CharField(max_length=100, default='/static/assets/img/book-no-cover.jpg')
	descricao = models.TextField()
	data = models.DateField(auto_now_add=True)

	ISBN = models.CharField(max_length=20)
	edicao = models.CharField(max_length=20)
	editora = models.CharField(max_length=20)
	dono = models.ForeignKey(Perfil, related_name="livros")

	RUIM = '1'
	BOM  = '2'
	NOVO = '3'

	ESTADO_OPCOES = (
 		(NOVO,'novo'),
 		(BOM,'bom'),
 		(RUIM,'ruim')
 	)

	estado = models.CharField(max_length=1, choices=ESTADO_OPCOES, default=BOM)

	def __str__(self):
		return self.titulo + ' by ' + self.autor

class Troca(models.Model):
	perfil_1 = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	perfil_2 = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="trocas")
	livro_1 = models.ForeignKey(Livro, on_delete=models.CASCADE)
	livro_2 = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="livros_trocados")
	nota_1 = models.IntegerField(default=1)
	nota_2 = models.IntegerField(default=1)
	avaliacao_1 = models.TextField(blank=True)
	avaliacao_2 = models.TextField(blank=True)
	concluida = models.BooleanField(default=False)
	data = models.DateField(auto_now_add=True)

class Mensagem(models.Model):
	data = models.DateField(auto_now_add=True)
	remetente = models.ForeignKey(Perfil, related_name='mensagens')
	troca = models.ForeignKey(Troca)
	conteudo = models.TextField()
	
	def __str__(self):
		return self.conteudo
