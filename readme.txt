Step - 1
pip3 install django-allauth
pip3 install django-crispy_forms

Step - 2
in installed apps add:
= [
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount', 
'allauth.socialaccount.providers.google',
'allauth.socialaccount.providers.facebook',
'allauth.socialaccount.providers.github',
'crispy_forms'

   ]

Step - 3

in context _processors in templates:
add - 'django.template.context_processors.request',

Step - 4

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
and add
SITE_ID = 1 (at bottom in settings page)
## add  last
----------
Step - 5

URLS:
from django.views.generic import TemplateView
urlpatterns = [

    path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('accounts/',include('allauth.urls')),

    ]

Step - 6 Change Allowed-Hosts = ['localhost']

Step - 7
now migrate

Step - 8 Create superuser:
Step - 9 Runserver

step - 10 go to admin page -> sites -> change domain name -> localhost:8000 and display name as localhost -> save


step - 11 
create google config in google and get the secret id & client id

50618996624-dasrmflncnqo6ve3av0212cmrtqkmce7.apps.googleusercontent.com client id
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 client secret

Step - 12

Go to admin page and add a social application
provider -> google
name -> Google (anything)
Client_id: '#clientid from google'
Secret key: '#secret key from google'
Key: no need to fill
sites: double click and add available sites 
and save

Step - 13
add - 

LOGIN_REDIRECT_URL = 'home'

ACCOUNT_LOGOUT_REDIRECT_URL = 'login'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
