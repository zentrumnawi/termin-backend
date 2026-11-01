from .base import *  # noqa


DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-tkghqim*+8e62rin#o81_&tm4o^r7m#_&if^7k*r+xe=!v%&m_",
)

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
# relevant if using django-cors-headers
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]
CORS_ALLOW_CREDENTIALS = True