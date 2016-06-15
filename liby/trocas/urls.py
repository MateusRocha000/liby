from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pendentes/$', views.pendentes, name='trocas'),
	url(r'^concluidas/$', views.concluidas, name='trocas'),
	url(r'^(?P<troca_id>\w+)$',	views.troca, 		name='trocas'),
	url(r'^nova/(?P<usuario_id>\w+)/(?P<livro_id>\w+)$',	views.nova, 		name='trocas'),	
	url(r'^mensagem/(?P<troca_id>\w+)$',	views.mensagem, 		name='trocas'),
	url(r'^selecionar/(?P<troca_id>\w+)/(?P<livro_id>\w+)$',	views.selecionar, 		name='trocas'),
]