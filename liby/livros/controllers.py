from home.models import *

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

def adicionarLivro(dono, titulo, autor, capa='', descricao='', isbn='', edicao='', editora='', estado=''):
	l = Livro()
	l.dono = dono
	l.titulo = titulo
	l.autor = autor

	if descricao:
		l.descricao = descricao

	if isbn:
		l.isbn = isbn
	
	if edicao:
		l.edicao = edicao

	if capa:
		l.capa = capa
		
	if editora:
		l.editora = editora		
	
	if estado:
		l.estado = estado
		
	l.save()

	return l