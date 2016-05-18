from home.models import *

def buscarUsuario(nome):
	return Perfil.objects.filter(nome__contains=nome)