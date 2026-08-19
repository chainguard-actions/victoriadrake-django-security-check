"""
Minimal Django settings for testing django-security-check action.
"""

SECRET_KEY = 'test-secret-key-for-action-testing-only'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
]

DATABASES = {}
