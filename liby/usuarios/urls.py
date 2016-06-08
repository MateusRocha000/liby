from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.usuarios, name='usuarios'),
	url(r'^buscar/$', views.buscar, name='buscar'),
	url(r'^seguindo/$', views.seguindo, name='buscar'),
	url(r'^(?P<usuario_id>\w+)$', views.usuario, name='usuario'),
	url(r'^seguir/(?P<usuario_id>\w+)$', views.seguir, name='usuario'),
]