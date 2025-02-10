# install auths
pip install django-allauth

# Add it to the INSTALLED_APPS array:
'django.contrib.sites'
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'

# To access the environment variables download load_dotenv from pip
pip install python-dotenv

from dotenv import load_dotenv

load_dotenv() # charge les variable d'environnement