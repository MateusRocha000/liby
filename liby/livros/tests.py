from django.test import TestCase

from home.models import *
from .controllers import *

class LivrosMethodTests(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='teste1')
        self.u2 = User.objects.create(username='teste2')
        self.p = Perfil.objects.create(nome="Saulo", user=self.u)
        self.p2 = Perfil.objects.create(nome="Saulo2", user=self.u2)
        self.l = Livro.objects.create(titulo="A menina que roubava livros", ISBN='9788598078373', dono=self.p)

    def test_meus_livros(self):
        self.assertIn(self.l, self.p.meusLivros())
        self.assertIsNotNone(self.p.meusLivros())

    def test_pesquisar_livro(self):
    	self.assertIn(self.l, buscarLivro('A menina'))
    	self.assertNotIn(self.l, buscarLivro('outrolivro'))

    def test_pesquisar_isbn(self):
        self.assertIn(self.l, buscarISBN('9788598078373'))
        self.assertNotIn(self.l, buscarISBN('000001'))

    def test_adicionar_livro(self):
        request = type('test', (object,), {'POST' : {}, 'user' : self.u})()
        request.POST = {
            'titulo' : "O guia do mochileiro",
            'autor' : "Douglas Adams",
            'capa': '',
            'descricao': '',
            'isbn': '',
            'editora': '',
            'edicao': '',
            'estado': '',
        }

        l = adicionarLivro(request)
        self.assertIn(l, self.p.meusLivros())

    def test_editar_livro(self):
        request = type('test', (object,), {'POST' : {}, 'user' : self.u})()
        request.POST = {
            'titulo' : "O guia do mochileiro",
            'autor' : "Douglas Adams",
            'capa': '',
            'descricao': '',
            'isbn': '',
            'editora': '',
            'edicao': '',
            'estado': '',
        }

        livro_id = self.l.id

        editarLivro(request, livro_id)
        self.assertEqual("O guia do mochileiro", Livro.objects.get(id=livro_id).titulo)
        self.assertEqual(0, len(buscarLivro('A menina')))
        self.assertEqual(1, len(buscarLivro('o guia do mochileiro')))

    def test_editar_livro_de_outro_usuario(self):
        request = type('test', (object,), {'POST' : {}, 'user' : self.u2})()
        request.POST = {
            'titulo' : "O guia do mochileiro",
            'autor' : "Douglas Adams",
            'capa': '',
            'descricao': '',
            'isbn': '',
            'editora': '',
            'edicao': '',
            'estado': '',
        }

        livro_id = self.l.id

        editarLivro(request, livro_id)
        self.assertEqual("A menina que roubava livros", Livro.objects.get(id=livro_id).titulo)
        self.assertEqual(1, len(buscarLivro('A menina')))
        self.assertEqual(0, len(buscarLivro('o guia do mochileiro')))

