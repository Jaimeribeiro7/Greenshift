ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
INSTALLED_APPS += [
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
