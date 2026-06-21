"""
Minimal Django settings for security check testing.
"""

SECRET_KEY = 'test-secret-key-for-security-check-action-testing-only'

DEBUG = False

ALLOWED_HOSTS = ['example.com']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/test.db',
    }
}

# Intentionally missing security settings so the check produces output
# (e.g., SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, etc.)
