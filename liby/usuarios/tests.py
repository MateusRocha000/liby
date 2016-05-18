from django.test import TestCase

from home.models import *
from .controllers import *

class UsuariosMethodTests(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='teste1')
        self.u2 = User.objects.create(username='teste2')
        self.p = Perfil.objects.create(nome="Saulo Antunes Silva", user=self.u)
        self.p2 = Perfil.objects.create(nome="ramon silva", user=self.u2)
        self.l = Livro.objects.create(titulo="A menina que roubava livros", ISBN='9788598078373', dono=self.p)

    def test_buscar_usuario(self):
        self.assertIn(self.p, buscarUsuario('saulo'))
        self.assertIn(self.p, buscarUsuario('SAULO'))
        self.assertIn(self.p, buscarUsuario('ANTUNES'))
        self.assertNotIn(self.p, buscarUsuario('ramon'))
        self.assertEqual(0, buscarUsuario('xxxxxx').count())
        self.assertGreaterEqual(2, len(buscarUsuario('')))
        self.assertGreaterEqual(2, len(buscarUsuario('silva')))