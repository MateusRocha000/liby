from django.test import TestCase
from home.models import *
from .controllers import *

class HomeMethodTests(TestCase):
    def setUp(self):
        self.u = User.objects.create(username='teste1')
        self.p = Perfil.objects.create(nome="Saulo", user=self.u)
        self.l = Livro.objects.create(titulo="A menina que roubava livros", ISBN='9788598078373', dono=self.p)

    def test_deletar_usuario(self):
        request = type('test', (object,), {'user' : self.u})()
        deletaConta(request)
        self.assertNotIn(self.u, User.objects.all())

    def test_verifica_remocao_dos_livros_apos_deletar_conta(self):
        request = type('test', (object,), {'user' : self.u})()
        deletaConta(request)
        self.assertNotIn(self.l, Livro.objects.all())     
