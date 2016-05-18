from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', 			views.usuarios, 		name='usuarios'),
	url(r'^buscar/$', 	views.buscar, 	name='buscar'),
]