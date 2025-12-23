from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    os.environ.get("RENDER_EXTERNAL_HOSTNAME")
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
        "OPTIONS": {
            "sslmode": "require"
        }
    }
}
