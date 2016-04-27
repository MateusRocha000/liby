from home.models import *

def set_profile(backend, response, user, is_new=False, *args, **kwargs):
    if backend.name == 'facebook':
        try:
            p = Perfil.objects.get(user=user)
        except Perfil.DoesNotExist:
            p = Perfil()
            p.user = user
        
        p.nome = response['name']
        p.foto = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        p.cidade = response['location']['name'].split(',')[0]
        p.save()

        print(response)