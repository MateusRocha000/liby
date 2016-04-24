# Usando python-social-auth para autenticação via facebook

1. Instalação

`$ pip install python-social-auth`

2. Configuração

**Keys**
```
SOCIAL_AUTH_FACEBOOK_KEY    = '1565959830363527'
SOCIAL_AUTH_FACEBOOK_SECRET = '5ee2a57ef7dcfbe204e825521d43f9a0'
```

**Backends**
```
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
```

**URLs**
```
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
```

**PIPELINE**

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'home.utils.set_profile',							# Função que irá armazerar as informações de perfil
)

**INSTALLED_APPS**
```
INSTALLED_APPS = (
    ...
    'social.apps.django_app.default',
    ...
)
```

**URLs**
```
urlpatterns = [
    ...
    url('', include('social.apps.django_app.urls', namespace='social')),
    ...
]
```

**Template Context Processors**
```
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    ...
)
```