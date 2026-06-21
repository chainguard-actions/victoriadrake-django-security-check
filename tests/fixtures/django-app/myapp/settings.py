"""
Minimal Django settings for testing django-security-check action.
These settings intentionally lack production security settings so that
`manage.py check --deploy` will report warnings/issues.
"""

SECRET_KEY = 'test-secret-key-not-for-production-use-only'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

DATABASES = {}

# Intentionally missing security settings so check --deploy reports issues:
# - No SECURE_SSL_REDIRECT
# - No SESSION_COOKIE_SECURE
# - No CSRF_COOKIE_SECURE
# - No SECURE_HSTS_SECONDS
