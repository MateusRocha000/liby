from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.usuarios, name='usuarios'),
	url(r'^buscar/$', views.buscar, name='usuarios'),
	url(r'^seguindo/$', views.seguindo, name='usuarios'),
	url(r'^seguidores/$', views.seguidores, name='usuarios'),
	url(r'^(?P<usuario_id>\w+)$', views.usuario, name='usuario'),
	url(r'^seguir/(?P<usuario_id>\w+)$', views.seguir, name='usuario'),
	url(r'^deixardeseguir/(?P<usuario_id>\w+)$', views.deixardeseguir, name='usuario'),
]