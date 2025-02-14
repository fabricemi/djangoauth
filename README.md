# install auths
pip install django-allauth

# Add it to the INSTALLED_APPS array:
'django.contrib.sites'
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'

  ##for boostrap
  'bootstrap5'

# To access the environment variables download load_dotenv from pip
pip install python-dotenv

from dotenv import load_dotenv

load_dotenv() # charge les variable d'environnement

# boostrap
pip install django-bootstrap-v5

# add to head balise of base templates
<head>
  {% load bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
</head>