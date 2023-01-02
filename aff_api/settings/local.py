from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-9g&el5ve&&tcvm+ra&&5-_yhd-w!$pefq0^tt9t1#=6c5s^roy",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

SITE_NAME = "Authors Haven"