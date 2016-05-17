from django.test import TestCase

from home.models import *
from .controllers import *

class LivrosMethodTests(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='teste1')
        self.p = Perfil.objects.create(nome="Saulo", user=self.u)
        self.l = Livro.objects.create(titulo="A menina que roubava livros", ISBN='9788598078373', dono=self.p)

    def test_meus_livros(self):
        self.assertIn(self.l, self.p.meusLivros())
        self.assertIsNotNone(self.p.meusLivros())

    def test_pesquisar_livro(self):
    	self.assertIn(self.l, buscarLivro('A menina'))
    	self.assertNotIn(self.l, buscarLivro('outrolivro'))

    def test_pesquisar_isbn(self):
        self.assertIn(self.l, buscarLivro('9788598078373'))
        self.assertNotIn(self.l, buscarLivro('000001'))

    def test_adicionar_livro(self):
    	l = adicionarLivro(dono=self.p, titulo="O guia do mochileiro", autor="Douglas Adams")
    	self.assertIn(l, self.p.meusLivros())