from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',					views.trocas, 		name='trocas'),
	url(r'^(?P<troca_id>\w+)$',	views.troca, 		name='trocas'),
]