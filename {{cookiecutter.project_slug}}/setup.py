#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requires = [
    # Wheel 0.25+ needed to install certain packages on CPython 3.5+
    # like Pillow and psycopg2
    # See http://bitly.com/wheel-building-fails-CPython-35
    # Verified bug on Python 3.5.1
    'wheel==0.29.0',

    'django==1.10.5',

    # Configuration
    'django-environ==0.4.1',

    {% if cookiecutter.use_whitenoise == 'y' -%}
    'whitenoise==3.2.3',
    {%- endif %}

    # Images
    'Pillow==4.0.0',

    # For user registration, either via email or social
    'django-allauth==0.30.0',

    # Python-PostgreSQL Database Adapter
    'psycopg2==2.6.2',

    # Unicode slugification
    'awesome-slugify==1.6.5',

    # Time zones support
    'pytz==2016.10',

    # Redis support
    'django-redis==4.7.0',
    'redis>=2.10.5'

    {% if cookiecutter.use_celery == "y" %}
    'celery==3.1.24',    {% endif %}

    'django-extensions==1.7.5',
    # Email backends for Mailgun, Postmark, SendGrid and more
    'django-anymail==0.7',
    # Static and Media Storage
    'boto==2.45.0',    'django-storages-redux==1.3.2',
    # Raven is the Sentry client
    'raven==5.32.0',
    # REST Api
    'djangorestframework==3.4.6',
    'drf-extensions==0.2.8',
    'djangorestframework_jwt==1.8.0',
    'django-cors-headers==1.1.0',

    # Filter support for our rest api
    'django-filter==0.13.0',

    # Expose django allauth via our REST API
    'django-rest-auth==0.8.1',
]


test_requires = [
    'coverage==4.3.1',
    'django-coverage-plugin==1.3.1',
    'factory-boy==2.8.1',
    'pytest-django==3.1.2',
    'pytest-sugar==0.8.0',
    'flake8==3.2.1',
    'mock==2.0.0',
    'fake-factory==0.5.6',
    'freezegun==0.3.6',
]


docs_requires = [
    'Sphinx==1.5.1',
    'sphinxcontrib-httpdomain==1.4.0',
    'sphinx_rtd_theme==0.1.9',
]


local_requires = [
    'django-debug-toolbar==1.6',

    # improved REPL
    'ipdb==0.10.1',
]


setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    # long_description=read('README.rst'),
    # url='https://bitbucket.org/minglabs/tra-01-backend',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    test_suite='src',
    tests_require=test_requires,
    install_requires=install_requires,
    extras_require={
        'tests': test_requires,
        'docs': docs_requires,
        'local': local_requires,
    },
    zip_safe=False,
    classifiers=[
        '__DO NOT UPLOAD__',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
