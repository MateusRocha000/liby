from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', 							views.livros, 		name='livros'),
	url(r'^meus-livros/$', 				views.meusLivros, 	name='livros'),
	url(r'^adicionar/$', 				views.adicionar, 	name='livros'),
	url(r'^buscar/$',		 			views.buscar, 		name='livros'),
	url(r'^buscarisbn/$',		 		views.buscarisbn, 	name='livros'),
	url(r'^excluir/(?P<livro_id>\w+)$',	views.excluir, 		name='livros'),
	url(r'^editar/(?P<livro_id>\w+)$',	views.editar, 		name='livros'),
	url(r'^(?P<livro_id>\w+)$',			views.livro, 		name='livros'),
]