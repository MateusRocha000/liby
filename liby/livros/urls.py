from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', 					views.livros, 		name='livros'),
	url(r'^meus-livros/$', 		views.meusLivros, 	name='livros'),
	url(r'^adicionar/$', 		views.adicionar, 	name='livros'),
	url(r'^buscar/$', 			views.buscar, 		name='livros'),
	url(r'^(?P<livro_id>\w+)$',	views.livro, 		name='livros'),
]