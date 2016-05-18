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

def editarLivro(request, livro_id):
	try:
		l = Livro.objects.get(id=livro_id, dono=request.user.perfil)
		l.titulo=request.POST['titulo']
		l.autor=request.POST['autor']
		l.capa=request.POST['capa']
		l.descricao=request.POST['descricao']
		l.ISBN=request.POST['isbn']
		l.edicao=request.POST['edicao']
		l.editora=request.POST['editora']
		l.estado=request.POST['estado']
		l.save()

		return l
		
	except:
		return False

def excluirLivro(request, livro_id):
	try:
		Livro.objects.get(id=livro_id, dono=request.user.perfil).delete()
		return True
	except:
		return False