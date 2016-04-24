SOCIAL_AUTH_FACEBOOK_KEY    = '1565959830363527'
SOCIAL_AUTH_FACEBOOK_SECRET = '5ee2a57ef7dcfbe204e825521d43f9a0'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

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
    'home.utils.set_profile',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_location']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, location', 
}