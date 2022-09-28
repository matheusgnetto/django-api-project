import environ
from api.settings.dev import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET KEY")

ALLOWED_HOSTS = env.list("ALLOWEB HOSTS")

DATABASES = {
    "default": env.db()
}
