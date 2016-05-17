from home.models import *
# from isbnlib import *

def buscarLivro(titulo='', autor=''):
	livros = None

	if titulo:
		livros = Livro.objects.filter(titulo__contains=titulo)

	if autor:
		if livros:
			livros &= Livro.objects.filter(autor__contains=autor)
		else:
			livros = Livro.objects.filter(autor__contains=autor)

	return livros

def buscarISBN(isbn=''):
	livros = None
	
	if isbn:				
		livros = Livro.objects.filter(ISBN__contains=isbn)


	return livros

def adicionarLivro(request):
	l = Livro.objects.create(titulo=request.POST['titulo'],
							 autor=request.POST['autor'],
							 capa=request.POST['capa'],
							 descricao=request.POST['descricao'],
							 ISBN=request.POST['isbn'],
							 edicao=request.POST['edicao'],
							 editora=request.POST['editora'],
							 estado=request.POST['estado'],
							 dono=request.user.perfil
							 )
	return l